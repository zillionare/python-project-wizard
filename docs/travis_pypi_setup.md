# PyPI Setup

Optionally, your package can automatically be released on PyPI whenever
you push a new tag to the master branch.

## Install the Travis CLI tool

This is OS-specific.

### macOS

We recommend the Homebrew travis package:

`` ` brew install travis ``\`

### Windows and Linux

Follow the official Travis CLI installationinstructions for your
operating system:

<https://github.com/travis-ci/travis.rb#installation>

## How It Works

Once you have the <span class="title-ref">travis</span> command - line
tool installed, from the root of your project do:

    travis encrypt --add deploy.password

This will encrypt your locally-stored PyPI password and save that to
your <span class="title-ref">.travis.yml</span> file. Commit that change
to git.

## Your Release Process

If you are using this feature, this is how you would do a patch release:

``` bash
bump2version patch
git push --tags
```

This will result in:

-   mypackage 0.1.1 showing up in your GitHub tags/releases page
-   mypackage 0.1.1 getting released on PyPI

You can also replace patch with <span class="title-ref">minor</span> or
<span class="title-ref">major</span>.

## More Details

You can read more about using Travis for PyPI deployment at:
<https://docs.travis-ci.com/user/deployment/pypi/>
