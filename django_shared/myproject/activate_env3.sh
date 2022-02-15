#!/bin/bash

echo "hello from bash script"
#on the commandline, run this: . /usr/myproject/activate_env3.sh 
#on subsequent runs, remove RUN mkdir /app 
cp -r /usr/myproject/ /app/
virtualenv -p python3 env3
. env3/bin/activate
pip3 install -r myproject/requirements.txt

