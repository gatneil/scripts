#!/bin/bash
while true; do
    ping -c 10 google.com;
    if [ $? -eq 0 ]
    then
	break;
    fi
done