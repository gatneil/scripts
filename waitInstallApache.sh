#!/bin/bash
sleep 30

apt-get -y update

apt-get -y install apache2 

apachectl restart