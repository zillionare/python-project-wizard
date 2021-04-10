# PyPI Release Checklist

## For Every Release

1.  Update HISTORY.rst

2.  Commit the changes:

    > ``` bash
    > git add HISTORY.rst
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

7.  Check the PyPI listing page to make sure that the README, release
    notes, and roadmap display properly. If tox test passwed, this should be ok, since
    we have already run twine check during tox test.

8.  Edit the release on GitHub (e.g.
    <https://github.com/audreyr/cookiecutter/releases>). Paste the
    release notes into the release's release page, and come up with a
    title for the release.

## About This Checklist

This checklist is adapted from:

-   <https://gist.github.com/audreyr/5990987>
-   <https://gist.github.com/audreyr/9f1564ea049c14f682f4>

It assumes that you are using all features of Cookiecutter PyPackage.
