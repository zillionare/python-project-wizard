# Cookiecutter PyPackage

Cookiecutter template for Python package, forked from [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

For those who don't know what cookiecutter is: cookiecutter is like a scaffold tool, a wizard which help you create new porject from template.

* [GitHub repo](https://github.com/zillionare/cookiecutter-pypackage/)
* [Documentation](https://zillionare.github.io/cookiecutter-pypackage/)
* Free software: BSD license

## Features

This template will create new Python project with the following features:

* [Poetry]: Manage version, dependancy, build and release
* [Mkdocs]: Writting your docs in markdown style
* Testing with unittest or [Pytest]
* Code coverage report and upload to [Codecov]
* [Tox]: Test your code against defined Python version matrix, lint and build artifact check.
* Format with [Black] and [Isort]
* Lint code with [Flake8] and [Flake8-docstrings]
* [Pre-commit hooks]: Formatting/linting anytime when commit/run local tox/CI
* [Mkdocstrings]: Auto API doc generation
* Command line interface using [Python Fire] (optional)
* CI by [github actions], auto publish from release branch when tests passed
* Host your documentation from [Git Pages] with zero-config

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)

```
  pip install -U cookiecutter
```

Generate a Python package project:

```
  cookiecutter https://github.com/zillionare/cookiecutter-pypackage.git
```
Then follow **[Tutorial](/tutorial)** to finish other configurations.

# Credits

This repo is forked from [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage), and borrowed some ideas from [briggySmalls](https://github.com/briggySmalls/cookiecutter-pypackage)


[poetry]: https://python-poetry.org/
[mkdocs]: https://www.mkdocs.org
[pytest]: https://pytest.org
[codecov]: https://codecov.io
[tox]: https://tox.readthedocs.io
[black]: https://github.com/psf/black
[isort]: https://github.com/PyCQA/isort
[flake8]: https://flake8.pycqa.org
[flake8-docstrings]: https://pypi.org/project/flake8-docstrings/
[mkdocstrings]: https://mkdocstrings.github.io/
[Python Fire]: https://github.com/google/python-fire
[github actions]: https://github.com/features/actions
[Git Pages]: https://pages.github.com
[Pre-commit hooks]: https://pre-commit.com/
