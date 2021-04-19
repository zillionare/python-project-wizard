# PyPI Release Checklist

## For Every Release

0.  Check out release branch, merge all changes from master/main to release

1.  Update HISTORY.md

    Be noticed that github workflow will generate a changelog for you automatically.

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

5.  Push the commit to release branch:

    > ``` bash
    > git push
    > ```

6.  Push the tags, creating the new release on both GitHub and PyPI:

    > ``` bash
    > git tag %tag_name%
    > git push --tags
    > ```

    tag_name has to be started with 'v'(lower case), to leverage github release workflow.

7.  Check the PyPI listing page to make sure that the README, release
    notes, and roadmap display properly. If tox test passwed, this should be ok, since
    we have already run twine check during tox test.

## About This Checklist

This checklist is adapted from:

-   <https://gist.github.com/audreyr/5990987>
-   <https://gist.github.com/audreyr/9f1564ea049c14f682f4>

It assumes that you are using all features of Cookiecutter PyPackage.
