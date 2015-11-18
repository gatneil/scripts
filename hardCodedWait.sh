#!/bin/bash
while true; do
    ping -c 10 8.8.8.8;
    if [ $? -eq 0 ]
    then
	break;
    fi
done

apt-get -y update

apt-get -y install apache2 

apachectl restart