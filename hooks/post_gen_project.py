#!/usr/bin/env python
import os
import sys
from hooks.aioproc import aioprocess, async_run
import colorama
from colorama import Fore, Style

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    try:
        os.remove(os.path.join(PROJECT_DIRECTORY, filepath))
    except FileNotFoundError:
        pass


@async_run
async def execute(*args, cwd=None):
    cur_dir = os.getcwd()

    proc = await aioprocess(*args, cwd=cwd)
    await proc.wait()


def init_git():
    # workaround for issue #1
    if not os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
        execute(
            "git",
            "config",
            "--system",
            "init.defaultBranch",
            "main",
            cwd=PROJECT_DIRECTORY,
        )
        execute("git", "init", cwd=PROJECT_DIRECTORY)
        execute(
            "git",
            "config",
            "user.name",
            "{{ cookiecutter.full_name }}",
            cwd=PROJECT_DIRECTORY,
        )
        execute(
            "git",
            "config",
            "user.email",
            "{{ cookiecutter.email }}",
            cwd=PROJECT_DIRECTORY,
        )


def init_dev():
    print(Style.NORMAL, Fore.BLUE, "installing pre-commit hooks...")
    print(Style.RESET_ALL, Style.DIM)
    try:
        execute(sys.executable, "-m", "pip", "install", "pre-commit")
        execute("pre-commit", "install", cwd="{{ cookiecutter.project_slug }}")
        print(Style.NORMAL, Fore.GREEN, "pre-commit hooks was successfully installed")
        print(Style.RESET_ALL)
    except Exception as e:
        print(e)
        print(
            Fore.YELLOW,
            "failed to install pre-commit hooks. You may need run `pre-commit install` later by your self",
            Style.RESET_ALL,
        )

    print(Style.NORMAL, Fore.BLUE, "installing poetry...")
    print(Style.RESET_ALL, Style.DIM)

    try:
        execute(sys.executable, "-m", "pip", "install", "poetry")
        print(Style.NORMAL, Fore.GREEN, "poetry installed successfully", Style.RESET_ALL)
    except Exception as e:
        print(e)
        print(
            Fore.YELLOW,
            "failed to install poetry, you may need re-run the task by yourself.",
            Style.RESET_ALL,
        )
        return

    try:
        print(Style.NORMAL, Fore.BLUE, "install all dev dependency packages...")
        print(Style.RESET_ALL, Style.DIM)
        execute("poetry", "install", "-E", "dev", "-E", "doc", "-E", "test", cwd=PROJECT_DIRECTORY)
        print(
            Style.NORMAL,
            Fore.GREEN,
            "all dev dependency packages installed successfully",
            Style.RESET_ALL,
        )
    except Exception as e:
        print(e)
        print(
            Style.NORMAL,
            Fore.YELLOW,
            "failed to install dev dependency packages, you may need re-run the task by yourself: poetry install -E dev -E test -E doc",
            Style.RESET_ALL,
        )



if __name__ == "__main__":
    colorama.init()

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.md")
        remove_file("docs/authors.md")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.project_slug }}", "cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    try:
        init_git()
    except Exception as e:
        print(e)

    if "{{ cookiecutter.init_dev_env }}" == "y":
        try:
            init_dev()
        except Exception as e:
            print(e)
