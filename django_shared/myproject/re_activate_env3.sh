#!/bin/bash

echo "hello again from bash script"
#on the commandline, run this: . /usr/myproject/re_activate_env3.sh
cp -r /app/myproject/ /usr/myproject/
cd /usr/myproject/ && virtualenv -p python3 env3
. /usr/myproject/env3/bin/activate
pip3 install -r /usr/myproject/requirements.txt
#ls /usr/myproject/

