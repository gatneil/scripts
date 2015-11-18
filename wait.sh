#!/bin/bash
while true; do
    ping -c 3 -W 3 bing.com;
    if [ $? -eq 0 ]
    then
	break;
    fi
done

apt-get -y update

apt-get -y install apache2 

apachectl restart