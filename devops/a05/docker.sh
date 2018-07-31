#!/bin/bash
if [ -z $1 ]
then
	echo 'Usage: docker.sh <name:[tag]>'
	echo 'Example: docker.sh ubuntu:14.04'
	exit 0
fi
docker pull $1
mkdir n5
cd n5
wget https://raw.githubusercontent.com/docker-library/python/cf179e4a7b442b29d85f521c2b172b89ef04beef/3.6/jessie/Dockerfile
docker build . -t jessie:python3.6
cont=`docker images | grep "python" | awk '{ print $3 }'`
docker run $cont /usr/local/bin/python3.6 -V
