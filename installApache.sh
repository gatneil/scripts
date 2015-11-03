#!/bin/bash
apt-get clean

apt-get -y update

apt-get -y install apache2 

apachectl restart