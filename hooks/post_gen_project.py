#!/usr/bin/env python
import os
import subprocess
import sys

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def execute(*args, supress_exception = False):
    proc = subprocess.Popen(args, stdout = subprocess.PIPE, stderr= subprocess.PIPE)

    out, err = proc.communicate()
    out = out.decode('utf-8')
    err = err.decode('utf-8')
    if err and not supress_exception:
        raise Exception(err)
    else:
        return out

def install_pre_commit_hooks():
    if not os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
        execute("git", "init")

    execute(sys.executable, "-m", "pip", "install", "pre-commit==2.12.0")
    execute("pre-commit", "install")

if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.md')
        remove_file('docs/authors.md')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if '{{ cookiecutter.install_precommit_hooks }}' == 'y':
        try:
            install_pre_commit_hooks()
        except Exception as e:
            print(str(e))
            print("Failed to install pre-commit hooks. Please run `pre-commit install` by your self. For more on pre-commit, please refer to https://pre-commit.com")
