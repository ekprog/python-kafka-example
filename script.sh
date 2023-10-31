#!/bin/bash

docker container run \
-itd \
--rm \
-v ${PWD}/output:/app/output \
--name pyscript \
pyscript:latest