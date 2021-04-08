# Cookiecutter PyPackage

Cookiecutter template for a Python package, forked from [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

For those who don't know what cookiecutter is: cookiecutter is like a scaffold tool, a wizard that help you create new porject from template.

* GitHub repo: https://github.com/zillionare/cookiecutter-pypackage/
* Documentation: https://zillionare.github.io/cookiecutter-pypackage/
* Free software: BSD license

## Features

This template will help you create new Python project that contains the following features:

* [Poetry](https://python-poetry.org/): Manage version, dependancy, build and release
* [Mkdocs](https://www.mkdocs.org): Writting your docs in markdown style
* Testing setup with unittest or [pytest](https://pytest.org)
* code coverage report
* [Travis-CI](https://www.travis-ci.com/): Test and deploy your product
* [Tox](https://tox.readthedocs.io): Test automation and standarized
* Code formatting/linting occurs at code commit and tox/CI
* Code formatting by [black](https://github.com/psf/black), [isort](https://github.com/PyCQA/isort)
* Code linting by [flake8](https://github.com/PyCQA/flake8)
* [mkdocstrings](https://mkdocstrings.github.io/) Auto API doc generation
* Command line interface using [Python Fire](https://github.com/google/python-fire) (optional)
* Documentation: support both git pages and readthedocs

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/zillionare/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis-CI account.
* Install the dev requirements into a virtualenv. (``poetry install -E doc -E dev -E test``)
* Run the Travis CLI command `travis encrypt --add deploy.password` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your Read the Docs account + turn on the Read the Docs service hook.
* Release your package by pushing a new tag to master.
* Get your code on! 😎 Add your package dependencies as you go, locking them into your virtual environment with ``poetry add``.

For more details, see the [cookiecutter-pypackage tutorial](https://zillionare.github.io/cookiecutter-pypackage/tutorial.html)

# Credits

This repo is forked from [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage), and borrowed some ideas from [briggySmalls](https://github.com/briggySmalls/cookiecutter-pypackage)
