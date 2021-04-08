# Prompts

When you create a package, you are prompted to enter these values.

## Templated Values

The following appear in various parts of your generated project.

full\_name  
Your full name.

email  
Your email address.

github\_username  
Your GitHub username.

project\_name  
The name of your new Python package project. This is used in
documentation, so spaces and any characters are fine here.

project\_slug  
The namespace of your Python package. This should be Python
import-friendly. Typically, it is the slugified version of
project\_name.

project\_short\_description  
A 1-sentence description of what your Python package does.

release\_date  
The date of the first release.

pypi\_username  
Your Python Package Index account username.

year  
The year of the initial package copyright in the license file.

version  
The starting version number of the package.

## Options

The following package configuration options set up different features
for your project.

use\_pypi\_deployment\_with\_travis  
Whether to use PyPI deployment with Travis.

command\_line\_interface  
Whether to create a console script using Python Fire. Console script
entry point will match the project\_slug. Options: \['Fire', "No
command-line interface"\]
