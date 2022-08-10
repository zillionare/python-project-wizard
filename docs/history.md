# History
!!! Info
    `(#{number})` means an issue of this project. You may check details of the issue by visiting https://github.com/zillionare/python-project-wizard/issues/_{number}_

## v1.2
* [#7](https://github.com/zillionare/python-project-wizard/issues/7) documentatioin will now support multiple versions
* [#8](https://github.com/zillionare/python-project-wizard/issues/8) add .docstring.tpl to project
* [#10](https://github.com/zillionare/python-project-wizard/issues/10) fixed.
* [#11](https://github.com/zillionare/python-project-wizard/issues/11) fixed.
* [#12](https://github.com/zillionare/python-project-wizard/issues/12) replaced.
* [#13](https://github.com/zillionare/python-project-wizard/issues/13) implemented. Only tested with vscode, please have autodocstrings extension installed.
* [#14](https://github.com/zillionare/python-project-wizard/issues/14) implemented.
* [#15](https://github.com/zillionare/python-project-wizard/issues/15) done.
* [#16](https://github.com/zillionare/python-project-wizard/issues/16) fixed
# v1.0
***first release with the following features:***

1. [Poetry]: Manage version, dependancy, build and release
2. [Mkdocs]: Writting your docs in markdown style
3. Testing with [Pytest] (unittest is still supported out of the box)
4. Code coverage report and endorsed by [Codecov]
* [Tox]: Test your code against environment matrix, lint and artifact check.
* Format with [Black] and [Isort]
* Lint code with [Flake8] and [Flake8-docstrings]
* [Pre-commit hooks]: Formatting/linting anytime when commit/run local tox/CI
* [Mkdocstrings]: Auto API doc generation
* Command line interface using [Python Fire] (optional)
* Continuouse Integration/Deployment by [github actions], includes:
    - publish dev build/official release to TestPyPI/PyPI automatically when CI success
    - publish documents automatically when CI success
    - extract change log from github and integrate with release notes automatically
* Host your documentation from [Git Pages] with zero-config


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
