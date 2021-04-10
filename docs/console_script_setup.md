# Console Script Setup

Optionally, your package can include a console script using [Fire]

# How It Works

If the `command_line_interface` option is set to `fire` during setup, cookiecutter
 will add a file `cli.py` in the project_slug subdirectory. An entry point is added to
pyproject.toml that points to the main function in cli.py.

# Usage

To use the console script in development:

``` bash
poetry install
```

`projectdir` should be the top level project directory with the
pyproject.toml file

Then execute:
```
    $your_package_name help
```

it will show your package name, project short description and exit.

# More Details

You can read more about Python Fire at [Fire]

[Fire]: https://google.github.io/python-fire/guide/
