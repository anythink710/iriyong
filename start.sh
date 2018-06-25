#!/bin/bash

git pull origin master
sudo service gunicorn restart
