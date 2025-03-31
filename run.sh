#!/bin/bash
#--------------
# Bash script for build and run a docker container for Flask
# web note-taking application

TAG=cs217-a3

docker build -t $TAG .

docker run -d -p 5001:5000 \
--rm \
-it \
-v ${PWD}/instance:/app/instance \
$TAG