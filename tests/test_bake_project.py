import datetime
import os
import shlex
import subprocess
import sys
from contextlib import contextmanager
from typing import List
from unittest import mock

import pytest
from cookiecutter.utils import rmtree

# logging.basicConfig(level=logging.DEBUG)


_DEPENDENCY_FILE = "pyproject.toml"
_INSTALL_DEPS_COMMANDS = [
    "poetry install",
]


def build_commands(commands):
    cmds = _INSTALL_DEPS_COMMANDS.copy()
    cmds.extend(commands)
    return cmds


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(commands, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param commands: Commands that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        for command in commands:
            subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    """Run a command from inside a given directory, returning the command output"""
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))

def execute(command: List[str], dirpath: str, timeout=30, supress_warning=True):
    """Run command inside given directory and returns output

    if there's stderr, then it may raise exception according to supress_warning
    """
    with inside_dir(dirpath):
        proc = subprocess.Popen(
            command, 
            stderr=subprocess.PIPE, 
            stdout=subprocess.PIPE
        )

    out, err = proc.communicate(timeout=timeout)
    out = out.decode('utf-8')
    err = err.decode('utf-8')

    if err and not supress_warning:
        raise RuntimeError(err)
    else:
        print(err)
        return out

def test_year_compute_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join('LICENSE')
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert _DEPENDENCY_FILE in found_toplevel_files
        assert 'python_boilerplate' in found_toplevel_files
        assert 'tox.ini' in found_toplevel_files
        assert 'tests' in found_toplevel_files

        mkdocs_yml = os.path.join(result._project_dir, "mkdocs.yml")
        with open(mkdocs_yml, "r") as f:
            lines = f.readlines()
            assert '  - authors: authors.md\n' in lines


def test_bake_without_author_file(cookies):
    with bake_in_temp_dir(
        cookies,
        extra_context={'create_author_file': 'n'}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'AUTHORS.md' not in found_toplevel_files
        doc_files = [f.basename for f in result.project.join('docs').listdir()]
        assert 'authors.md' not in doc_files     

        # make sure '-authors: authors.md' not appeared in mkdocs.yml
        mkdocs_yml = os.path.join(result._project_dir, "mkdocs.yml")
        with open(mkdocs_yml, "r") as f:
            lines = f.readlines()
            assert '  - authors: authors.md\n' not in lines

@pytest.mark.parametrize("license_info", [
    ('MIT', 'MIT '),
    ('BSD-3-Clause', 'Redistributions of source code must retain the ' +
     'above copyright notice, this'),
    ('ISC', 'ISC License'),
    ('Apache-2.0', 'Licensed under the Apache License, Version 2.0'),
    ('GPL-3.0-only', 'GNU GENERAL PUBLIC LICENSE'),
])
def test_bake_selecting_license(cookies, license_info):
    license, target_string = license_info
    with bake_in_temp_dir(
        cookies,
        extra_context={'open_source_license': license}
    ) as result:
        assert target_string in result.project.join('LICENSE').read()
        assert license in result.project.join(_DEPENDENCY_FILE).read()


def test_bake_not_open_source(cookies):
    with bake_in_temp_dir(
        cookies,
        extra_context={'open_source_license': 'Not open source'}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert _DEPENDENCY_FILE in found_toplevel_files
        assert 'LICENSE' not in found_toplevel_files
        assert 'License' not in result.project.join('README.md').read()
        assert 'license' not in result.project.join(_DEPENDENCY_FILE).read()


def test_not_using_pytest(cookies):
    with bake_in_temp_dir(cookies, extra_context={'use_pytest': 'n'}) as result:
        assert result.project.isdir()
        # Test pyproject doesn't install pytest
        dep_file_path = result.project.join(_DEPENDENCY_FILE)
        lines = dep_file_path.readlines()
        assert "pytest = \"*\"\n" not in lines
        # Test contents of test file
        test_file_path = result.project.join('tests/test_python_boilerplate.py')
        lines = test_file_path.readlines()
        assert "import unittest" in ''.join(lines)
        assert "import pytest" not in ''.join(lines)


def test_docstrings_style(cookies):
    with bake_in_temp_dir(cookies, extra_context={'docstrings_style': 'google'}) as result:
        assert result.project.isdir()
        # Test lint rule contains google style
        flake8_conf_file_apth = result.project.join(".flake8")
        lines = flake8_conf_file_apth.readlines()
        assert "docstring-convention = google" in ''.join(lines)


# def test_project_with_hyphen_in_module_name(cookies):
#     result = cookies.bake(
#         extra_context={'project_name': 'something-with-a-dash'}
#     )
#     assert result.project is not None
#     project_path = str(result.project)
#
#     # when:
#     travis_setup_cmd = ('python travis_pypi_setup.py'
#                         ' --repo audreyr/cookiecutter-pypackage'
#                         ' --password invalidpass')
#     run_inside_dir(travis_setup_cmd, project_path)
#
#     # then:
#     result_travis_config = yaml.load(
#         open(os.path.join(project_path, ".travis.yml"))
#     )
#     assert "secure" in result_travis_config["deploy"]["password"],\
#         "missing password config in .travis.yml"


@pytest.mark.parametrize("args", [
    ({'command_line_interface': "No command-line interface"}, False),
    ({'command_line_interface': 'fire'}, True),
])
def test_bake_with_no_console_script(cookies, args):
    context, is_present = args
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)
    assert ("cli.py" in found_project_files) == is_present

    pyproject_path = os.path.join(project_path, _DEPENDENCY_FILE)
    with open(pyproject_path, 'r') as pyproject_file:
        assert ('[tool.poetry.scripts]' in pyproject_file.read()) == is_present


def test_bake_with_console_script_cli(cookies):
    context = {'command_line_interface': 'fire'}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    module_path = os.path.join(project_dir, 'cli.py')

    out = execute([sys.executable, module_path], project_dir)
    assert f"is one of the following:{os.linesep}{os.linesep}     help{os.linesep}" in out

    out = execute([sys.executable, module_path, "help"], project_dir)

    assert project_slug in out
