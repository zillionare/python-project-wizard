# Tutorial

??? Note
    Did you find this article confusing? [Edit this file] and pull a request!

To start with, you will need [GitHub], [Pypi] , [TestPyPi] and [Codecov] account. If 
you don't have one, please follow the links to apply one before you get started on this 
tutorial. 

If you are new to Git and GitHub, you should probably spend a few minutes on
some of the tutorials at the top of the page at [GitHub Help]

## Step 1: Install Python Project Wizard (ppw)

Install ppw:

``` bash
pip install ppw
```

## Step 2: Generate Your Package

Now it's time to generate your Python package.

Run the following command and feed with answers:

```bash
  ppw
```

Finally a new folder will be created under current folder, the name is the answer you
provided to `project_slug`.

The project layout should looks like:

```
.
├── AUTHORS.md
├── CONTRIBUTING.md
├── .coveragerc
├── dist
├── docs
│   ├── api.md
│   ├── authors.md
│   ├── contributing.md
│   ├── history.md
│   ├── index.md
│   ├── installation.md
│   └── usage.md
├── .editorconfig
├── .flake8
├── .github
│   ├── ISSUE_TEMPLATE.md
│   └── workflows
│       ├── dev.yml
│       └── release.yml
├── .gitignore
├── HISTORY.md
├── .isort.cfg
├── LICENSE
├── mkdocs.yml
├── poetry.lock
├── ppw_0420_01
│   ├── cli.py
│   ├── __init__.py
│   └── ppw_0420_01.py
├── .pre-commit-config.yaml
├── pyproject.toml
├── pyrightconfig.json
├── README.md
├── site
├── tests
│   ├── __init__.py
│   └── test_ppw_0420_01.py
└── tox.ini
```

Here the project_slug is ppw_0420_01, when you genereate yours, it could be other name.

Also be noticed that there's pyproject.toml in this folder. This is the main
configuration file of our project.

## Step 3: Build a virtual environment for your development
Now build a virtual python environment for your development, and develop your project 
always in that environment from now on.

You can choose either annaconda or virtualenv. I prefer annaconda (actually miniconda) 
though.

```
conda create -n mypackage python=3.8
conda activate mypackage
conda install -c conda-forge tox-conda
```

You could choose your favorite python version here. 
## Step 4: Install Dev Requirements

You should still be in the folder named as `%proejct_slug`, which containing the
 `pyproject.toml` file.

Install the new project's local development requirements inside a
virtual environment:

``` bash
pip install poetry
poetry install -E doc -E dev -E test
tox
```

We start with install poetry, since the whole project is managed by poetry. Then we
installed extra dependency need by developer, such as documentation build tools, lint, 
formatting and test tools etc.

We also launch a smoke test here by running `tox`. This will give you a test report and
 lint report. You should see no errors except some lint warnings.

??? Tips

    Extra dependencies are grouped into three groups, doc, dev and test for better 
    granularity. When you ship the package, dependencies in group doc, dev and test 
    might not be shipped.

    As the developer, you will need install all the dependencies.

??? Tips

    if you found erros like the following during tox run:
    ```
    ERROR: InterpreterNotFound: python3.9
    ```
    don't be panic, this is just because python3.x is not found on your machine. If you
    decide to support that version of Python in your package, please install it on your
    machine. Otherwise, remove it from tox.ini and pyproject.toml (search python3.x then
    remove it).

## Step 5: Create a GitHub Repo

Go to your GitHub account and create a new repo named `mypackage`, where
`mypackage` matches the `[project_slug]` from your answers to running
cookiecutter.

Then goto repo > settings > secrets, click on 'New repository secret', add the following
 secrets:

- TEST_PYPI_API_TOKEN, see [How to apply testpypi token]
- PYPI_API_TOKEN, see [How to apply pypi token]
- PERSONAL_TOKEN, see [How to apply personal token]

## Step 6: Set Up codecov integration

???+ Tips

    If you have already setup codecov integration and configured access for all your 
    repositories, you can skip this step.

In your browser, visit [install codecov app], you'll be landed at this page:

![](http://images.jieyu.ai/images/202104/20210419175222.png)

Click on the green `install` button at top right, choose `all repositories` then click
on `install` button, following directions until all set.

## Step 7: Upload code to github

Back to your develop environment, find the folder named after the `[project_slug]`. 
Move into this folder, and then setup git to use your GitHub repo and upload the
code:

``` bash
cd mypackage

git add .
git commit -m "Initial skeleton."
git branch -M main
git remote add origin git@github.com:myusername/mypackage.git
git push -u origin main
```

Where `myusername` and `mypackage` are adjusted for your username and
package name.

You'll need a ssh key to push the repo. You can [Generate] a key or
[Add] an existing one.

???+ Warning

    if you answered 'yes' to the question if install pre-commit hooks at last step, 
    then you should find pre-commit be invoked when you run `git commit`, and some files
     may be modified by hooks. If so, please add these files and **commit again**.

### Check result

After pushing your code to github, goto github web page, navigate to your repo, then
click on actions link, you should find screen like this:

![](http://images.jieyu.ai/images/202104/20210419170304.png)

There should be one workflow running. After it finished, go to [testpyi], check if a
new artifact is published under the name {{ cookiecutter.project_slug }}

## Step 8. Check documentation

  Documentation will be published and available at 
  <https://{your_github_account}.github.io/{your_repo}> once:

    1. the branch is release
    2. the commit is tagged, and the tag name is started with 'v' (lower case)
    3. build/testing executed by github CI passed

  If you'd like to see what it's look like now, you could run the followng command:

  ```
  mkdocs gh-deploy
  ```

  then check your documentation at <https://{your_github_account}.github.io/{your_repo}>

## Step 9. Make official release

  After done with your phased development, switch to releas branch, following 
  instructions at [release checklist](/pypi_release_checklist), trigger first official release and check
  result at [PYPI].


[Edit this file]: https://github.com/zillionare/cookiecutter-pypackage/blob/master/docs/tutorial.md
[Codecov]: https://codecov.io/
[PYPI]: https://pypi.org
[GitHub]: https://github.com/
[TestPyPI]: https://test.pypi.org/
[GitHub Help]: https://help.github.com/
[Generate]: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
[Add]: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
[How to apply testpypi token]: https://test.pypi.org/manage/account/
[How to apply pypi token]: https://pypi.org/manage/account/
[How to apply personal token]: https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
[install codecov app]: https://github.com/apps/codecov
