#!/usr/bin/env bash

VIRTUALENV_NAME=${PWD##*/}
mkvirtualenv $VIRTUALENV_NAME
pip install -r "requirements.txt"

