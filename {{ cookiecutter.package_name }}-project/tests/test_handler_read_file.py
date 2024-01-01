# -*- coding: utf-8 -*-

from {{ cookiecutter.package_name }}.handlers.read_file import handler, path_file


def test():
    sf = handler.handler("")
    assert len(sf.items) == 1
    assert sf.items[0].subtitle == path_file.read_text()


if __name__ == "__main__":
    from {{ cookiecutter.package_name }}.tests import run_cov_test

    run_cov_test(__file__, "{{ cookiecutter.package_name }}.handlers.read_file", preview=False)
