#!/bin/bash

if [ -f ~/.i3/comp ]
then
    rm ~/.i3/comp
    killall compton
    killall glava
    notify-send --expire-time=5000 "Compositing disabled"
else
    touch ~/.i3/comp
    compton -b
    glava &
    notify-send --expire-time=5000 "Compositing enabled"
fi
