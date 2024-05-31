#!/bin/sh

echo "BACKEND_IP=$BACKEND_IP"
# Replace backend IP in the environment.prod.ts file
sed -i "s|<backend-service-ip>|$BACKEND_IP|g" /usr/share/nginx/html/main*.js

# Start Nginx
nginx -g 'daemon off;'
