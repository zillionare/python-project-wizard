"""Console script for {{cookiecutter.project_slug}}."""

{% if cookiecutter.command_line_interface|lower == 'fire' -%}
import fire

def help():
    print(f"{{ cookiecutter.project_slug }}")

def main():
    fire.Fire({
        "help": help,
        "--help": help
    })


if __name__ == "__main__":
    main() # pragma: no cover
{%- endif %}
