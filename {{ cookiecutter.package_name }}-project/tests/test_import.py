# -*- coding: utf-8 -*-

import os
import pytest
import {{ cookiecutter.package_name }}


def test_import():
    _ = {{ cookiecutter.package_name }}.wf


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
