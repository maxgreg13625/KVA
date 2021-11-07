#!/bin/bash

# remove stopped container
sudo docker ps --filter status=exited -q | xargs sudo docker rm
# remove pre-built image
yes | sudo docker image prune -a

# re-built docker image
sudo docker build -t kva-test . --no-cache