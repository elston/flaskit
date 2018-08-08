#!/bin/bash
docker run -it --rm \
-v kubcenter_router_letsencrypt:/etc/letsencrypt \
-v kubcenter_router_letsencrypt_data:/router/letsencrypt \
certbot/certbot \
renew \
--webroot \
--webroot-path=/router/letsencrypt
