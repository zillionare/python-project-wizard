<div id="console-script-setup">

Console Script Setup =================

</div>

Optionally, your package can include a console script using Click or
argparse (Python 3.2+).

# How It Works

If the 'command\_line\_interface' option is set to \['fire'\] during setup, cookiecutter
 will add a file 'cli.py' in the project\_slug subdirectory. An entry point is added to
pyproject.toml that points to the main function in cli.py.

# Usage

To use the console script in development:

``` bash
pip install -e projectdir
```

'projectdir' should be the top level project directory with the
pyproject.toml file

The script will be generated with output for no arguments and --help.

--help  
show help menu and exit

# More Details

You can read more about Python Fire at [](https://google.github.io/python-fire/guide/)
