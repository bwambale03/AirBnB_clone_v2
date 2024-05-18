#!/usr/bin/env bash
# A bash script that sets up web servers for the deployment of web static
# Install nginx if not installed already
# Creates the required directories
# Creates a fake HTML file for test
# Create a symbolic link
# Sets ownership of folder, updates and restarts nginx
# Exits successfully

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

cat <<EOF | sudo tee /data/web_static/releases/test/index.html
<html>
<head>
    <title>Test HTML file</title>
</head>
<body>
    Holberton School
</body>
</html>
EOF

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server;/a \\n\\ location /hbnb_static {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default

sudo service nginx restart

exit 0

