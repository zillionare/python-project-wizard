
??? Note
    Did you find this article confusing? [Edit this file] and pull a request!

To start with, you will need [GitHub], [Pypi] , [TestPyPi] and [Codecov] account. If you don't have one, please follow the links to apply one before getting started on this tutorial.

If you are new to Git and GitHub, you should probably spend a few minutes on some of the tutorials at [GitHub Help]

## Step 1: Install Python Project Wizard (ppw)

We'll need `ppw` to generate a skeleton project. Following the instructions to install `ppw` on to your machine. 

``` bash
pip install ppw
```

If virtual environment is used during your developement, install `ppw` as global.
## Step 2: Build a virtual environment for your development
It's best practice that always developing your project in dedicated python virtual environment. So let's start from creating a virtual environment now:

You may choose either annaconda or virtualenv， annaconda (actually miniconda) is preferred though.

```
conda create -n mypackage python=3.8
conda activate mypackage
conda install -c conda-forge tox-conda
```

Choose python version on your own decision. Be noticed that we're now at a virtual env called `mypackage`
## Step 3: Generate Your Package

!!!Important
    Make sure run the following command under `mypackage` virtual env.

Now it's time to generate your Python package.

Run the following command and feed with answers:

```bash
  ppw
```

Finally a new folder will be created under current folder, the name is the answer you
provided to `project_slug`.

At last step, it'll ask you `ppw` should performe initialization for you. If the answer is 'yes', then `ppw` will:

1. install pre-commit hooks
2. install poetry
3. install necessary dependencies which required by test and documentation. These deps will include pytest, tox, mkdocs and etc.

The project layout should look like:

```
.
├── AUTHORS.md
├── CONTRIBUTING.md
├── .coveragerc
├── .docstring.tpl
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
│   └── app.py
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

Here the project_slug is ppw_0420_01. When you genereate yours, it could be other name.

Also be noticed that there's pyproject.toml in this folder. This is the main
configuration file of our project.

You could choose your favorite python version here.
## Step 4: Install Dev Requirements

!!!Important
    Skip this step if you've answered 'yes' to the question `init_dev_env`. They're performed automatically if the answer is 'yes'.

You should still be in the folder named as `%proejct_slug`, which containing the
 `pyproject.toml` file.

Install the new project's local development requirements inside a
virtual environment:

``` bash
pip install poetry
poetry install -E doc -E dev -E test
```

We started with installing poetry, since the whole project is managed by poetry. Then we
installed extra dependency need by developer, such as documentation building tools, lint,
formatting and testing tools etc.

## Step 5: Smoke test
Run the following command now:
```
tox
```

This will give you a test report and a lint report. You should see no errors except some lint warnings.

???+ Tips

    Extra dependencies are grouped into three groups, doc, dev and test for better
    granularity. When you ship the package, dependencies in group doc, dev and test
    might not be shipped.

    As the developer, you will need install all the dependencies.

??? Tips

    if you found erros like the following during tox runs:
    ```
    ERROR: InterpreterNotFound: python3.9
    ```
    don't be panic, this is just because python3.x is not found on your machine. If you
    decide to support that version of Python in your package, please install it on your
    machine. Otherwise, remove it from tox.ini and pyproject.toml (search python3.x then
    remove it).

## Step 6: Create a GitHub Repo

Go to your GitHub account and create a new repo named `mypackage`, where
`mypackage` matches the `[project_slug]` from your answers when running `ppw`

Then goto repo > settings > secrets, click on 'New repository secret', add the following
 secrets:

- TEST_PYPI_API_TOKEN, see [How to apply testpypi token]
- PYPI_API_TOKEN, see [How to apply pypi token]
- PERSONAL_TOKEN, see [How to apply personal token]

## Step 7: Setup codecov integration

???+ Tips

    If you have already setup codecov integration and configured access for all your
    repositories, you can skip this step.

In your browser, visit [install codecov app], you'll be landed at this page:

![](http://images.jieyu.ai/images/202104/20210419175222.png)

Click on the green `install` button at top right, choose `all repositories` then click
on `install` button, following directions until all sets.

## Step 8: Upload code to github

Back to your develop environment, find the folder named after the `[project_slug]`.
Go to this folder, and then setup git to use your GitHub repo and upload the
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

You'll need a ssh key to push the repo. You could [Generate] a key or
[Add] an existing one.

???+ Warning

    if you answered 'yes' to the question if `init_dev_env` at last step,
    then you should find `pre-commit` was invoked when you run `git commit`, and some files
     may be modified by hooks. If so, please add these files and **commit again**.

### Step 9: Check the CI result

After pushing your code to github, go to github web page, navigate to your repo, then
click on actions link, you should find screen like this:

![](http://images.jieyu.ai/images/202104/20210419170304.png)

There should be one workflow running. After it finished, go to [testpyi], check if a
new artifact is published under the name {{ cookiecutter.project_slug }}

## Step 10. Check the documentation

  Documentation will be published and available at
  <https://{your_github_account}.github.io/{your_repo}> once:

    1. the branch is either main or master
    2. the commit is tagged, and the tag name is started with 'v' (lower case)
    3. build/testing executed by github CI passed

  If you'd like to see what it looks like now, you could run the followng command:

  ```
  mkdocs gh-deploy
  ```

  then check your documentation at <https://{your_github_account}.github.io/{your_repo}>

  or you can serve it locally by:

  ```
  mkdocs serve -a 0.0.0.0:8000
  ```
  
  then open your browser, visit your dev machine on port 8000.

???+ Info
    Though we used mkdocs here, however, in order to support multiple versions of documentation, we actually use mike in github actions.

???+ Important
    ppw choose github pages to host your documentation. you need visit https://github.com/{github_account}/{your_repo}/settings/pages to enable it:

    ![](https://images.jieyu.ai/images/20220820220812134811.png)

    the above pages shows example on how to configure it.

## Step 11. Make an official release

    After done with your phased development, switch to either of (main, master) branch, following instructions at [release checklist](/python-project-wizard/pypi_release_checklist), trigger first official release and check result at [PYPI].
  
## Step 12. Customization

ppw assume some settings for you, for example, it choose python version in pyproject.toml and tox.ini. You may need change the according to you case.

The following section will address how to customize github workflow:
### customize github workflow

    You may need to customize settings in workflow. Open .github/workflows/dev.yml:
    ```
    jobs:
    test:
        # The type of runner that the job will run on
        strategy:
        matrix:
            python-versions: ['3.7,' '3.8',' 3.9', '3.10']
            # github action doesn't goes well with windows due to docker support
            # github action doesn't goes well with macos due to `no docker command`
            #os: [ubuntu-20.04, windows-latest, macos-latest]
            os: [ubuntu-20.04]
        runs-on: ${{ matrix.os }}
    ```
    you may need to change python-version and os here. If you need to change python version, make sure never use 3.10 (rather than '3.10'). The former one will is actually equal to 3.1, according to yaml's parser.

    We need run build & publish job on one platform & python version only. So ppw have seperate test job from "build & publish" job, and you have to change `runs-on` and `python-version` accordingly too.

    ```
    publish_dev_build:
        # if test failed, we should not publish
        needs: test
        # you may need to change os below
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v2
        - uses: actions/setup-python@v2
            with:
            # you may need to change python version below
            python-version: '3.9'
    ```

    ppw also provide example configuration about how to use service and webhooks (Dingtalk notification robot), but it's disabled by default. Uncomment these lines to enable it:
    ```
    # uncomment the following to pickup services
    # services:
    #   redis:
    #     image: redis
    #     options: >-
    #       --health-cmd "redis-cli ping"
    #       --health-interval 10s
    #       --health-timeout 5s
    #       --health-retries 5
    #     ports:
    #       - 6379:6379
    ```

    ```
    # - name: Dingtalk Robot Notify
    #   uses: leafney/dingtalk-action@v1.0.0
    #   env: 
    #     DINGTALK_ACCESS_TOKEN: ${{ secrets.DINGTALK_ACCESS_TOKEN }}
    #     DINGTALK_SECRET: ${{ secrets.DINGTALK_SECRET }}
    #   with:
    #     msgtype: markdown
    #     notify_when: 'success'
    #     title: CI Notification | Success
    #     text: |
    #       ### Build success
    #       ${{ env.package_version_full }} is built and published to test pypi
    #       ### Change History
    #       Please check change history at https://${{ env.repo_owner }}.github.io/${{ env.repo_name }}/history
    #       ### package download
    #       Please download the pacakge at: https://test.pypi.org/project/${{ env.repo_name }}/
    ```

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
