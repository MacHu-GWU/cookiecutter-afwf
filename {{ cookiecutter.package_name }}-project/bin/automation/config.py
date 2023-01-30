# -*- coding: utf-8 -*-

"""
Automation config management.
"""

import dataclasses
from pathlib_mate import Path


@dataclasses.dataclass
class AutomationConfig:
    python_version: str = dataclasses.field()
    dir_workflow: Path = dataclasses.field()


config = AutomationConfig(
    python_version="3.8",
    dir_workflow=Path(
        "{{ cookiecutter.dir_workflow }}"
    ),
)
