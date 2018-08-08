#!/bin/bash

# ...env
mkdir -p /$PROJECT/.env
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv $PROJECT
pip install -r /tmp/requirements.txt

# ...logs
mkdir -p /$PROJECT/.logs
echo '' > /$PROJECT/.logs/main.log