# -*- coding: utf-8 -*-

from ._version import __version__

__license__ = "MIT"
__author__ = "{{ cookiecutter.author_name }}"
__author_email__ = "{{ cookiecutter.author_email }}"
__github_username__ = "{{ cookiecutter.github_username }}"
__chore__ = "dc2ba0d33e28cbfd762ab8579bcb8483"

try:
    from .workflow import wf
except ImportError: # pragma: no cover
    pass