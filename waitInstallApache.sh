#!/bin/bash

# wait till network settles down
sleep 60

apt-get -y update

apt-get -y install apache2 

apachectl restart