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
    # Why mkdocs over sphinx?
    reStructured Text and Sphinx is way to tedious, though powerful. With extension, 
    you'll find almost all features are available in mkdocs, in a neat and productive 
    way. Poetry and Markdown, are the two key factors driven me develop this template.

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
