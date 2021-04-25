#!/bin/sh

docker build -t criskrus/jupyter -f .docker/jupyter/Dockerfile .

docker run --rm --user root -p 8888:8888 -v $(pwd):/home/cristian.suarez/notebooks -e NB_UID=$(id -u) -e NB_GID=$(id -g) criskrus/jupyter