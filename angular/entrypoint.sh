#!/bin/sh

echo "BACKEND_IP=$BACKEND_IP"
current_date=$(TZ="Europe/Paris" date +'%Y-%m-%d %H:%M:%S')

# Replace backend IP in the environment.prod.ts file
sed -i "s|<backend-service-ip>|$BACKEND_IP|g" /usr/share/nginx/html/main*.js
sed -i "s|<build-date>|$current_date|g" /usr/share/nginx/html/main*.js

# Start Nginx
nginx -g 'daemon off;'
