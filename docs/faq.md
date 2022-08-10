
???+ Question
    # Why not travis CI?
    Travis CI is a great service, however, github actions is super convenient, less configuration
    , better integration. Less configuration, less error prone.

???+ Question
    # Why not read the docs?
    Same reason as above. Git pages is convenient than read the docs, it requires no
    further configuration, except access token. As to read the docs, you need to
    write v2 config file, plus several settings on web pages.

???+ Question
    # Why mkdocs instead of sphinx?
    reStructured Text and Sphinx is way to tedious, though powerful. With extension,
    you'll find almost all features are available in mkdocs, in a neat and productive
    way. Poetry and Markdown, are the two key factors driven me develop this template.

???+ How to trigger a release build?
    Once you've tagged either of (main, master) branch with `v`(for example, v1.0), then github actions will trigger a release build and finally publish documentation to https://{your_github_account}.github.io/{your_repo_slug} and push a wheels to pypi.

    You can also manually trigger this one:
    ```
    git tag -a v1.0 -m "Release v1.0"
    git push --tags
    ```
    then check on github to see if actions is executing. Once it's done successfully.

???+ How to manually publish documentation?
    By default, every push to github will trigger a documentation dev build, with the name is ${poetry version --short}-dev. And every tag starts with 'v' on main/master branch will cause a release build, and documentation will be built too.

    However, by any chances, you can manually build and publish your documentation with:

    ```
    poetry run mike deploy -p `poetry version --short`
    poetry run mike set-default -p `poetry version --short`
    ```
    The above commands simply build documentation locally and push to github, then github will publish it.

???+ Question
    # What are the configuration items?

    Here is a list:

    ```
    ## Templated Values

    The following appear in various parts of your generated project.

    full_name
    Your full name.

    email
    Your email address.

    github_username
    Your GitHub username.

    project_name
    The name of your new Python package project. This is used in
    documentation, so spaces and any characters are fine here.

    project_slug
    The namespace of your Python package. This should be Python
    import-friendly. Typically, it is the slugified version of
    project_name.

    project_short_description
    A 1-sentence description of what your Python package does.

    release_date
    The date of the first release.

    pypi_username
    Your Python Package Index account username.

    year
    The year of the initial package copyright in the license file.

    version
    The starting version number of the package.

    install_precommit_hooks
    If you choose yes, then cookiecutter will install pre-commit hooks for you.

    docstrings_style
    one of `google, numpy, rst`. It's required by flake8-docstrings.

    ## Options

    The following package configuration options set up different features
    for your project.

    command_line_interface
    Whether to create a console script using Python Fire. Console script
    entry point will match the project_slug. Options: \['fire', "No
    command-line interface"\]
    ```

    except above settings, for CI/CD, you'll also need configure gitub repsitory secrets
    at page repo > settings > secrtes, and add the following secrets:

    - PERSONAL_TOKEN (required for publishing document to git pages)
    - TEST_PYPI_API_TOKEN (required for publishing dev release to testpypi)
    - PYPI_API_TOKEN (required for publish )

???+ Question
    # first launch of pre-commit failed

    first time launch `pre-commit run` failed with error: "[WARNING] The 'rev' field of
    repo 'https://github.com/ambv/black' appears to be a mutable reference
    (moving tag / branch)"

    Please follow the instructions to update pre-commit then run again.
