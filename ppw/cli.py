import os

def main():
    repo = "https://github.com/zillionare/cookiecutter-pypackage.git"
    os.system(f"cookiecutter -s {repo}")
