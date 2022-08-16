#!/bin/bash

# Personal token with full access rights is required to run this scripts
# Once you got persona token, set enviroment variable GH_TOKEN with it

# Uncomment the following to config github secret used by github workflow. 
gh secret set PERSONAL_TOKEN --body $GH_TOKEN
gh secret set PYPI_API_TOKEN --body $PYPI_API_TOKEN
gh secret set TEST_PYPI_API_TOKEN --body $TEST_PYPI_API_TOKEN

# uncomment the following if you need to setup email notification
gh secret set BUILD_NOTIFY_MAIL_SERVER --body $BUILD_NOTIFY_MAIL_SERVER
gh secret set BUILD_NOTIFY_MAIL_FROM --body $BUILD_NOTIFY_MAIL_FROM
gh secret set BUILD_NOTIFY_MAIL_PASSWORD --body $BUILD_NOTIFY_MAIL_PASSWORD
gh secret set BUILD_NOTIFY_MAIL_RCPT --body $BUILD_NOTIFY_MAIL_RCPT
gh secret set DINGTALK_ACCESS_TOKEN --body $DINGTALK_ACCESS_TOKEN
gh secret set DINGTALK_SECRET --body $DINGTALK_SECRET

# uncomment the following to create repo and push code to github
# git add ./{{cookiecutter.project_slug}}
# git commit -m "Initial commit by ppw"
# gh repo create {{cookiecutter.project_slug}} --public -s ./{{cookiecutter.project_slug}} --push
