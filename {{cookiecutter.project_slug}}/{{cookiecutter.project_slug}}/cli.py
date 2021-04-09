"""Console script for {{cookiecutter.project_slug}}."""

{% if cookiecutter.command_line_interface|lower == 'fire' -%}
import fire

def help():
    print("{{ cookiecutter.project_slug }}")
    print("=" * len("{{ cookiecutter.project_slug }}"))
    print("{{ cookiecutter.project_short_description }}")

def main():
    fire.Fire({
        "help": help
    })


if __name__ == "__main__":
    main() # pragma: no cover
{%- endif %}
