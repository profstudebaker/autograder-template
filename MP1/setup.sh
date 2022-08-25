#!/usr/bin/env bash
# install python3 and java dependencies to container
apt-get install -y python3 python3-pip python3-dev
apt-get -y install openjdk-11-jdk
# install gradescope utils via requirements.txt 
# (other packages can be added to this file)
pip3 install -r /autograder/source/requirements.txt
