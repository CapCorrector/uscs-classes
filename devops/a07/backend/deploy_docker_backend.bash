#!/bin/bash

# Stop and remove existing docker entries
echo *** Stop webserver
docker stop fileservice > /dev/null

echo *** Remove webserver image
docker rm fileservice > /dev/null

# Build nameko service from Vagrant host
echo *** Build nameko service
cd /vagrant/fileservice
docker build . -t u:backend

# Start docker daemon. Rabbitmq used to communicate with frontend runs on port 5672. Map this to port 5672 on the Vagrant host
echo *** Run backend service 
docker run -d --restart=always --name fileservice -p 5672:5672 u:backend

