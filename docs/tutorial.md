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

## Step 3: Build a virtual environment for your development
Now build a virtual python environment for your development, and develop your project 
always in that environment from now on.

You can choose either annaconda or virtualenv. I prefer annaconda (actually miniconda) 
though.

```
conda create -n mypackage python=3.8
conda activate mypackage
```

## Step 4: Install Dev Requirements

You should still be in the folder containing the `pyproject.toml` file.

Install the new project's local development requirements inside a
virtual environment using pipenv:

``` bash
pip install poetry
poetry install -E doc -E dev -E test
tox
```

We start with install poetry, since the whole project is managed by poetry. Then we
installed extra dependency need by developer, such as documentation build tools, lint, 
formatting and test tools etc.

We did a smoke test at last by running `tox`. This will give you a test report and lint
report. You should see no errors except some lint warnings.

??? Tips
    Extra dependencies are grouped into three groups, doc, dev and test for better 
    granularity. When you ship the package, dependencies in group doc, dev and test will
     not be shipped.

    As the developer, you will need install all the dependencies.

??? Tips
  if you found erros like the following during tox run:
  ```
  ERROR: InterpreterNotFound: python3.9
  ```
  don't be panic, this is just because python3.x is not found on your machine. If you
  decide to support that version of Python in your package, please install it on your
  machine. Otherwise, remove it from tox.ini and pyproject.toml (search python3.x then
  remove it))

## Step 5: Create a GitHub Repo

Go to your GitHub account and create a new repo named `mypackage`, where
`mypackage` matches the `[project_slug]` from your answers to running
cookiecutter.

You will find one folder named after the `[project_slug]`. Move into
this folder, and then setup git to use your GitHub repo and upload the
code:

``` bash
cd mypackage

# !!! uncomment the following line, if you didn't choose install pre-commit hooks at 
# last step. If you chose 'yes', then cookiecutter have already done that for you, since 
# pre-commit install need repo exist.

# git init
git add .
git commit -m "Initial skeleton."
git branch -M main
git remote add origin git@github.com:myusername/mypackage.git
git push -u origin main
```

Where `myusername` and `mypackage` are adjusted for your username and
package name.

You'll need a ssh key to push the repo. You can [Generate][] a key or
[Add][] an existing one.

??? Tips
  if you have asked to install pre-commit hooks at last step, then you should find
  pre-commit is running when you run `git commit`, and some files may be changed by
  hooks. If so, please add these files and commit again

## Step 6: Publish your package...to testpypi
  You can try to build and publish your package to test pypi, if it works well, so be
  true with real pypi.

  1. config testpypi repo by:
  ```
  poetry config repositories.testpypi https://test.pypi.org/legacy/
  ```

  2. in case you haven't register testpyi account, please visit 
  [testpypi](https://test.pypi.org/)  and register account, and create an upload token 
  under `account settings` pages

  3. run the following command to publish your package to testpypi:
  ```
  poetry publish --build -r testpypi
  ```
  your will be prompted with account and password, use `__token__` as username, and your
  token as password.
## Step 7. Set Up Github Actions

  Once you've pushed your files  github repo, github actions will be all set, except
  for one thing: you need configure secrets for deployment.

  Here is the procedures:

  Go to your repo's setting page, find `Environments` menu at the left sidebar, then
  click `New environment` button, create a new environment (I'd prefer `CI` as its
  name):

  Then add secrets into this environment. Secrets should include:

  - TEST_PYPI_API_TOKEN
  - PYPI_API_TOKEN, which you should apply on at [PYPI]

## Step 8. Set Up codecov integration

  This template already baked [codecov] in. You don't need to set token for codecov,
  however, you should grant access to your repo for codecov. This can be done at either
  side, github or codecov.

  You can logon to [codecov], sign in with your github account, then add new repository
  to codecov.

## Step 9. Set up readthedocs integration

  The template has baked [readthedocs] in, all you need is just goto [readthedos]

  [readthedocs]: https://readthedocs.org
  [codecov]: https://codecov.io/
  [PYPI]: https://pypi.org
  [Edit this file]: https://github.com/zillionare/cookiecutter-pypackage/blob/master/docs/tutorial.md
  [GitHub account]: https://github.com/
  [PyPI]: https://pypi.python.org/pypi
  [GitHub Help]: https://help.github.com/
  [Generate]: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
  [Add]: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
