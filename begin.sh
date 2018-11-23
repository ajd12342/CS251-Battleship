#!/bin/bash
sudo apt install python-dev
sudo apt install python3-pip
sudo apt install redis-server
sudo apt install net-tools
pip3 install -U django == 2.1.3
pip3 install -U django-crispy-forms == 1.7.2
pip3 install -U channels == 2.1.5
pip3 install -U channels-redis == 2.3.1
pip3 install -U django-picklefield == 1.1.0

if [ $# -ne 1 ];
then
  echo "Usage: sudo bash begin.sh <server_ip>";
  exit 1;
fi
  
bash run.sh "$1"
