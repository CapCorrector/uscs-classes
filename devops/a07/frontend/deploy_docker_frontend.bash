#!/bin/bash

# Stop and remove existing docker entries

echo *** Stopping frontend process
docker stop frontend > /dev/null

echo *** Removig frontend process
docker rm Frontend > /dev/null

# Build frontend from inside Vagrant host
echo *** Build  frontend
cd /vagrant/frontend
docker build . -t u:frontend

# Start docker frontend service in background as frontend
echo *** Run frontend and map to port 8000 on Vagrant host
docker run -d --restart=always --name frontend -p 8000:8000 u:frontend

