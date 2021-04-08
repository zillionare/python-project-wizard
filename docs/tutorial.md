# Tutorial

<div class="note">

<div class="title">

Note

</div>

Did you find any of these instructions confusing? [Edit this file][] and
submit a pull request with your improvements!

</div>

To start with, you will need a [GitHub account][] and an account on
[PyPI][]. Create these before you get started on this tutorial. If you
are new to Git and GitHub, you should probably spend a few minutes on
some of the tutorials at the top of the page at [GitHub Help][].

## Step 1: Install Cookiecutter

Install cookiecutter:

``` bash
pip install cookiecutter
```

We'll also need poetry so \[install that
too\](<https://python-poetry.org/docs/#installation>):

## Step 2: Generate Your Package

Now it's time to generate your Python package.

Use cookiecutter, pointing it at the cookiecutter-pypackage repo:

``` bash
cookiecutter https://github.com/zillionare/cookiecutter-pypackage.git
```

You'll be asked to enter a bunch of values to set the package up. If you
don't know what to enter, stick with the defaults.

## Step 3: Create a GitHub Repo

Go to your GitHub account and create a new repo named `mypackage`, where
`mypackage` matches the `[project_slug]` from your answers to running
cookiecutter.

You will find one folder named after the `[project_slug]`. Move into
this folder, and then setup git to use your GitHub repo and upload the
code:

``` bash
cd mypackage
git init .
git add .
git commit -m "Initial skeleton."
git remote add origin git@github.com:myusername/mypackage.git
git push -u origin master
```

Where `myusername` and `mypackage` are adjusted for your username and
package name.

You'll need a ssh key to push the repo. You can [Generate][] a key or
[Add][] an existing one.

## Step 4: Install Dev Requirements

You should still be in the folder containing the `pyproject.toml` file.

Install the new project's local development requirements inside a
virtual environment using pipenv:

``` bash
poetry install -E doc -E dev -E test
```

??? Tips
    Extra dependencies are grouped into three groups, doc, dev and test for better 
    granularity. When you ship the package, dependencies in group doc, dev and test will
     not be shipped.

    Since you're the developer, so you will need install all the dependencies.

## Step 5: Set Up Github Actions

It should be worked already after your very first push. It's all set!

  [Edit this file]: https://github.com/zillionare/cookiecutter-pypackage/blob/master/docs/tutorial.md
  [GitHub account]: https://github.com/
  [PyPI]: https://pypi.python.org/pypi
  [GitHub Help]: https://help.github.com/
  [Generate]: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
  [Add]: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
