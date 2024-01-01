# -*- coding: utf-8 -*-

"""
The upstream concrete repo is ``afwf_example-project``. This script can convert
the concrete repo into a project template.
"""

import shutil
from pathlib import Path
from cookiecutter_maker.maker import Maker

dir_here: Path = Path(__file__).absolute().parent
dir_tmp = dir_here.joinpath("tmp")
if dir_tmp.exists():
    shutil.rmtree(dir_tmp)
dir_tmp.mkdir(parents=True, exist_ok=True)
dir_home = Path.home()

maker = Maker.new(
    # the input concrete project directory
    input_dir=Path.home().joinpath("Documents", "GitHub", "afwf_example-project"),
    # the output template project directory
    output_dir=dir_tmp,
    # define the pair of ``concrete string`` and ``parameter name``
    mapper=[
        ("afwf_example", "package_name", "your_package_name_with_underscore"),
        ("afwf-example", "package_name_slugify", "your-package-name-with-underscore"),
        ("MacHu-GWU", "github_username", "your_github_username"),
        ("Sanhe Hu", "author_name", "Author Name"),
        ("husanhe@gmail.com", "author_email", "author@email.com"),
        (
            str(dir_home.joinpath("Documents/Alfred-Setting/Alfred.alfredpreferences/workflows/user.workflow.0339BCA6-FE73-4208-9B64-9DD64F6CB346")),
            "dir_workflow",
            str(dir_home.joinpath("path/to/Alfred.alfredpreferences/workflows/user.workflow.ABCD1234-A1B2-C3D4-E5F6-A1B2C3D4E5F6")),
        ),
        ("0.2.1", "semantic_version", "0.1.1"),
    ],
    # define what to include in the input directory
    # it is the relative path from the input directory
    # the rule is 'explicit exclude' > 'explicit include' > 'default include'
    include=[],
    # define what to exclude in the input directory
    # it is the relative path from the input directory
    exclude=[
        # dir
        ".venv",
        ".pytest_cache",
        ".git",
        ".idea",
        "build",
        "dist",
        "htmlcov",
        "__pycache__",
        "tmp",
        "docs/source/afwf_example",
        # file
        ".coverage",
    ],
    # overwrite the output location if already exists
    overwrite=True,
    # mapper could have one key is substring of another key
    # if this is True, it will ignore the error
    ignore_mapper_error=False,
    # when mapper could have one key is substring of another key
    # it will prompt you to confirm to continue
    skip_mapper_prompt=False,
    # do you want to print debug information?
    debug=True,
)
maker.templaterize()
