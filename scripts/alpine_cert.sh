#!/bin/bash
# ..
source ../books/global.sh
# ..
docker run \
-v $(pwd)/../data:/backup \
-v ${PROJECT}_router_letsencrypt:/router/letsencrypt_cert \
-v ${PROJECT}_router_letsencrypt_data:/router/letsencrypt_data \
-it --rm \
alpine \
/bin/sh