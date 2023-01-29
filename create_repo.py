# -*- coding: utf-8 -*-

"""
Create Python Github Repository file skeleton at ``/path-to/cookiecutter-pygitrepo/tmp/{{ cookiecutter.repo_name }}``
"""

from __future__ import print_function, unicode_literals
from superjson import json
from pathlib_mate import Path
from cookiecutter.main import cookiecutter

dir_here = Path(__file__).absolute().parent

if __name__ == "__main__":
    # read config from cookiecutter-afwf.json
    path_cookiecutter_afwf_json = Path(dir_here, "cookiecutter-afwf.json")
    data = json.loads(path_cookiecutter_afwf_json.read_text(), ignore_comments=True)
    del data["_please_ignore_this"]

    # dump context data to cookiecutter.json
    path_cookiecutter_json = Path(dir_here, "cookiecutter.json")
    path_cookiecutter_json.write_text(json.dumps(data, indent=4))

    # clean up existing environment
    dir_output = Path(dir_here, "tmp")
    dir_output.remove_if_exists()
    dir_output.mkdir_if_not_exists()

    # create project skeleton
    cookiecutter(
        template=dir_here.abspath,
        output_dir=dir_output.abspath,
        no_input=True,
    )
