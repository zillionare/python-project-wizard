{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
<p align="center">
<a href="https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}">
    <img src="https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg"
        alt = "Release Status">
</a>

<a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions">
    <img src="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/main.yml/badge.svg?branch=release" alt="CI Status">
</a>

<a href="https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/">
    <img src="https://img.shields.io/website/https/{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/index.html.svg?label=docs&down_message=unavailable&up_message=available" alt="Documentation Status">
</a>
{% if cookiecutter.add_pyup_badge == 'y' %}
<a href="https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/">
<img src="https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg" alt="Updates">
</a>
{% endif %}
</p>
{% else %}
{% if cookiecutter.add_pyup_badge == 'y' %}
<p>
<a href="https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/">
<img src="https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg" alt="Updates">
</a>
</p>
{% endif %}
{% endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: <https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/>
{% endif %}

## Features

* TODO

## Credits

This package was created with the [ppw](https://zillionare.github.io/python-project-wizard) tool. For more information, please visit the [project page](https://zillionare.github.io/python-project-wizard/).
