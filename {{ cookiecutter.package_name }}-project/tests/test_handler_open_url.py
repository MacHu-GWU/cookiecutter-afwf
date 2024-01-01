# -*- coding: utf-8 -*-

from {{ cookiecutter.package_name }}.handlers.open_url import handler


def test():
    sf = handler.handler("")
    assert len(sf.items) == 3


if __name__ == "__main__":
    from {{ cookiecutter.package_name }}.tests import run_cov_test

    run_cov_test(__file__, "{{ cookiecutter.package_name }}.handlers.open_url", preview=False)
