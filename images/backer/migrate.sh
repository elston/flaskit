#!/bin/bash
# ...
source /$PROJECT/.env/$PROJECT/bin/activate     
cd /$PROJECT
flask db upgrade