#!/bin/bash

if [ -f ~/.i3/clight ]
then
    rm ~/.i3/clight
    killall clight
    notify-send --expire-time=2000 "Automatic backlight disabled"
else
    touch ~/.i3/clight
    clight &
    notify-send --expire-time=2000 "Automatic backlight enabled"
fi
