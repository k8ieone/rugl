#!/bin/sh
act=$(echo "reboot
poweroff
hibernate
suspend
logout" | dmenu)
if [ $? -eq 0 ]
then
    if [[ $act=="logout" ]]
    then
        killall nm-applet
        killall redshift-gtk
        killall /usr/bin/python2 /usr/bin/indicator-cpufreq
        killall /usr/lib/notification-daemon-1.0/notification-daemon
        killall mpd
        killall blueman-applet
        i3-nagbar -t warning -m 'You pressed the exit shortcut. Do you really want to exit i3? This will end your X session.' -B 'Yes, exit i3' 'i3-msg exit'
        #pkill -u `id -u $USER`
    else
        systemctl $act -i
    fi
else
    exit 1
fi
