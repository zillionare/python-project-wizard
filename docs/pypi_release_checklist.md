
## For Every Release

0.  Merge your changes from features/release branch to master/main.

1.  Update HISTORY.md

    Be noticed that github workflow will generate a changelog for you automatically, but you'll have to make your own history.md.

2.  Commit the changes:

    > ``` bash
    > git add HISTORY.md
    > git commit -m "Changelog for upcoming release 0.1.1."
    > ```

3.  Update version number (can also be patch or major)

    > ``` bash
    > poetry patch
    > ```

4.  Run the tests:

    > ``` bash
    > tox
    > ```

5.  Push the commit to main branch:

    > ``` bash
    > git push
    > ```

6.  Push the tags, creating the new release on both GitHub and PyPI:

    > ``` bash
    > git tag -a v`poetry version --short` -m "my great release"
    > git push --tags
    > ```

    tag_name has to be started with 'v'(lower case), to leverage github release workflow.

7.  Check the PyPI listing page to make sure that the README, release
    notes, and roadmap display properly. If tox test passed, this should be ok, since
    we have already run twine check during tox test.

???+ Info
    # About This Checklist

    This checklist is adapted from:

    -   <https://gist.github.com/audreyr/5990987>
    -   <https://gist.github.com/audreyr/9f1564ea049c14f682f4>

    It's assumed that you are using all features of [Python Project Wizard](https://zillionare.github.io/python-project-wizard).
