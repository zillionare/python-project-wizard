# History

## v1.3.3
*[#31](https://github.com/zillionare/python-project-wizard/issues/31) Use peotry to create test environment when running tox
## v1.3.2
*[#28](https://github.com/zillionare/python-project-wizard/issues/28) Send notification mail whenever build success or failed
*[#27](https://github.com/zillionare/python-project-wizard/issues/27) failed to send build notfication mail due to no from field
## v1.3.1
*[#26](https://github.com/zillionare/python-project-wizard/issues/26) use mike to deploy multiple version of documentation directly, removed github action peaceiris/actions-gh-pages@v3 
## v1.3
* [#23](https://github.com/zillionare/python-project-wizard/issues/23) add email notification upon build success
* [#24](https://github.com/zillionare/python-project-wizard/issues/24) config repo secrets by script
* [#25](https://github.com/zillionare/python-project-wizard/issues/25) support create repo and upload source code
## v1.2.2
* [#22](https://github.com/zillionare/python-project-wizard/issues/22) mike deploy failed
## v1.2.1
* [#21](https://github.com/zillionare/python-project-wizard/issues/21) add environment variable: repo_name and repon_owner
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
* [#18](https://github.com/zillionare/python-project-wizard/issues/18) fixed
* [#19](https://github.com/zillionare/python-project-wizard/issues/19) implemented.
* [#20](https://github.com/zillionare/python-project-wizard/issues/20) implemented. You can refer by using ${{ env.package_version_short }} and ${{ env.package_version_full }} now.
## v1.0
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
