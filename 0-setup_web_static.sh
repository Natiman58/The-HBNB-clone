#!/bin/bash

# Check if Nginx is installed
if ! command -v nginx &> /dev/null; then
    echo "Nginx is not installed. Installing Nginx..."

    # Update package list
    sudo apt-get update

    # Install Nginx
    sudo apt-get install -y nginx

    # Start Nginx service
    sudo service nginx start
    echo "Nginx has been installed and started."
else
    echo "Nginx is already installed."
fi

# Create /data/ directory if it doesn't exist
if [ ! -d "data" ]; then
    mkdir -p data
    echo "Created directory data."
else
    echo "Data directory already exists."
fi

# Create /data/web_static/ directory if it doesn't exist
if [ ! -d "data/web_static" ]; then
    mkdir -p data/web_static
    echo "Created directory data/web_static."
else
    echo "Data/web_static directory already exists."
fi

# Create /data/web_static/releases/ directory if it doesn't exist
if [ ! -d "data/web_static/releases" ]; then
    mkdir -p data/web_static/releases
    echo "Created directory data/web_static/releases."
else
    echo "Data/web_static/releases directory already exists."
fi

# Create /data/web_static/shared/ directory if it doesn't exist
if [ ! -d "data/web_static/shared" ]; then
    mkdir -p data/web_static/shared
    echo "Created directory data/web_static/shared."
else
    echo "Data/web_static/shared directory already exists."
fi

# Create /data/web_static/releases/test/ directory if it doesn't exist
if [ ! -d "data/web_static/releases/test" ]; then
    mkdir -p data/web_static/releases/test
    echo "Created directory data/web_static/releases/test."
else
    echo "Data/web_static/releases/test directory already exists."
fi

# Create a fake HTML file
if [ ! -f "data/web_static/releases/test/index.html" ]; then
    touch data/web_static/releases/test/index.html
    echo "Created file data/web_static/releases/test/index.html."
else
    echo "Data/web_static/releases/test/index.html file already exists."
fi

# create a symbolic link called /data/web_static/current; if not exists
if [ ! -L "data/web_static/current" ]; then
    ln -s data/web_static/releases/test/ data/web_static/current
    echo "Created symbolic link: data/web_static/current"
else
    # otherwise delete and recreate everytime
    rm -rf data/web_static/current
    echo "Deleted existing symbolic key: /data/webs_tatic/current"
fi

# change the owner of /data/ folder to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

service nginx restart