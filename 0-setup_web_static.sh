#!/usr/bin/env bash
# A bash script that sets up web servers for the deployment of web static
# Install nginx if not installed already
# Creates the required directories
# Creates a fake HTML file for test
# Create a symbolic link
# Sets ownership of folder, updates and restarts nginx
# Exits successfully

# Update package list and install nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create required directories if they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Create a symbolic link, if it already exists, recreate it
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server;/a \\n\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo service nginx restart

# Exit successfully
exit 0

