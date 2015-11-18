#!/bin/bash
while true; do
    ping -c 10 -W 1 bing.com;
    if [ $? -eq 0 ]
    then
	break;
    fi
done

apt-get -y update

apt-get -y install apache2 

apachectl restart