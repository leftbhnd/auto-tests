#!/bin/bash
sudo apt-get install -y scrot
sudo pip install virtualenv==20.4.7
virtualenv -p /usr/bin/python env
source env/bin/activate
pip install -r requirements.txt
