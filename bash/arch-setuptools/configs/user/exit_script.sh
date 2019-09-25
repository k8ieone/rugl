#!/bin/sh
act=$(echo "reboot
poweroff
hibernate
suspend" | dmenu) 
systemctl $act
