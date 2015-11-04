#!/bin/bash

# wait till network settles down
while true; do
    ping -c 10 google.com;
    if [ $? -eq 0 ]
    then
	break;
    fi
done

apt-get -y update

apt-get -y install apache2 

apachectl restart