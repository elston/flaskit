#!/bin/bash

source /$PROJECT/.env/$PROJECT/bin/activate  
cd /$PROJECT
# ..
gunicorn app:app \
    --workers=5 \
    --bind=0.0.0.0:8000 \
    --log-file=-