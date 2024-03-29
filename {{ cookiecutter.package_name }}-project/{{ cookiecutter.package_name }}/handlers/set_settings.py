# -*- coding: utf-8 -*-

"""
[CN]

该 Script Filter 的功能是让用户对用作 settings 的 sqlite 写入. 可以和 ``view_settings.py``
模块配合使用查看效果.
"""

import typing as T
import sys

import attrs
import afwf.api as afwf

from ..settings import settings, SettingsKeyEnum


@attrs.define
class SetSettingValueHandler(afwf.Handler):
    def main(self, key: str, value: str) -> afwf.ScriptFilter:
        sf = afwf.ScriptFilter()
        settings[key] = value
        return sf

    def parse_query(self, query: str):
        key, value = query.split(" ", 1)
        return dict(
            key=key,
            value=value,
        )

    def encode_query(self, key: str, value: str) -> str:
        return f"{key} {value}"


set_setting_value_handler = SetSettingValueHandler(id="set_setting_value")


@attrs.define
class Handler(afwf.Handler):
    def main(
        self,
        key: T.Optional[str] = None,
        value: T.Optional[str] = None,
    ) -> afwf.ScriptFilter:
        sf = afwf.ScriptFilter()

        if key is None:
            for settings_key in SettingsKeyEnum:
                item = afwf.FuzzyItem(
                    title=settings_key.value,
                    subtitle=f"set {settings_key.value} to ...",
                    autocomplete=settings_key.value + " ",
                ).set_fuzzy_match_name(settings_key.value)
                sf.items.append(item)
        elif value is None:
            items = list()
            for settings_key in SettingsKeyEnum:
                item = afwf.FuzzyItem(
                    title=settings_key.value,
                    subtitle=f"set {settings_key.value} to ...",
                    autocomplete=settings_key.value + " ",
                ).set_fuzzy_match_name(settings_key.value)
                items.append(item)
            matcher = afwf.FuzzyItemMatcher.from_items(items)
            sf.items.extend(matcher.match(key, threshold=0))
        else:
            if key in SettingsKeyEnum.__members__:
                item = afwf.Item(
                    title=f"Set settings.{key} = {value!r}",
                )
                item.send_notification(
                    title=f"Set settings.{key} = {value!r}",
                )
                cmd = set_setting_value_handler.encode_run_script_command(
                    bin_python=sys.executable,
                    key=key,
                    value=value,
                )
                item.run_script(cmd)
                sf.items.append(item)
            else:
                item = afwf.Item(
                    title=f"{key!r} is not a valid settings key",
                )
                item.set_icon(afwf.IconFileEnum.error)
                sf.items.append(item)
        return sf

    def parse_query(self, query: str):
        q = afwf.Query.from_str(query)
        if q.n_trimmed_parts == 0:
            return dict(key=None, value=None)
        elif q.n_trimmed_parts == 1:
            return dict(key=q.trimmed_parts[0], value=None)
        elif q.n_trimmed_parts == 2:
            return dict(key=q.trimmed_parts[0], value=q.trimmed_parts[1])
        else:
            raise NotImplementedError


handler = Handler(id="set_settings")
