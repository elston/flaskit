#!/bin/bash
# ..
source ../books/global.sh
# ..
docker run -it --rm \
-v ${PROJECT}_router_letsencrypt:/etc/letsencrypt \
-v ${PROJECT}_router_letsencrypt_data:/router/letsencrypt \
certbot/certbot \
certonly \
--agree-tos \
--webroot \
--webroot-path=/router/letsencrypt \
--email derbok@mail.ru \
--rsa-key-size 4096 \
--authenticator webroot \
--domains flaskit.ru \
--domains www.flaskit.ru
