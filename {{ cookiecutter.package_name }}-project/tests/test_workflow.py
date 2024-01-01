# -*- coding: utf-8 -*-

from {{ cookiecutter.package_name }}.workflow import wf
from {{ cookiecutter.package_name }}.handlers import (
    error,
    memorize_cache,
    open_file,
    open_url,
    read_file,
    set_settings,
    view_settings,
    write_file,
)
from rich import print as rprint


def test():
    sf = wf._run(arg=f"{memorize_cache.handler.id} my_key")


if __name__ == "__main__":
    from {{ cookiecutter.package_name }}.tests import run_cov_test

    run_cov_test(__file__, "{{ cookiecutter.package_name }}.workflow", preview=False)
