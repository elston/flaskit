#!/bin/bash
# ...
source /$PROJECT/.env/$PROJECT/bin/activate     
cd /$PROJECT
flask run --host ${FLASK_HOST} --port ${FLASK_PORT}