#!/bin/bash

# _random=$(zenity --width=400 --height=275 --list --radiolist --title 'Mac Changer' --text 'Select mode:' --column 'Select' --column 'Mode' TRUE "Random MAC" FALSE "Enter MAC manually")

# Colors!
red=$(tput setaf 1)
green=$(tput setaf 2)
reset=$(tput sgr0)

# Kindly ask the user to start this script with sudo
echo
echo "${red}Please make sure this scripts runs with root privileges.${reset}"
echo

# List network interfaces and make an array with them
_interfaces=($(ls /sys/class/net))
counter=0
for _interface in ${_interfaces[*]}
do
    counter=$(expr $counter + 1)
    echo "$counter. $_interface"
done

# Ask the user wich interface to use
echo -n "Please select your interface: "
read -r _interface
echo
echo "You selected ${_interfaces[$(expr $_interface - 1)]}"

# Ask if you want to change or revert to hardware MAC
echo "Do you want to revert to reset you MAC to the hardware one?"
echo -n "(y/N): "
read -r _choice
if [[ $_choice == y* ]]
then
    ip link set ${_interfaces[$(expr $_interface - 1)]} down
    sleep 1
    macchanger -p ${_interfaces[$(expr $_interface - 1)]}
    sleep 1
    ip link set ${_interfaces[$(expr $_interface - 1)]} up
    exit 0
else
    :
fi

# Ask if you want a random MAC address or enter one manually
echo
echo "Do you want a random MAC address or enter one manually?"
echo -n "(random/manual): "
read -r _choice
if [[ $_choice == random ]]
then
    ip link set ${_interfaces[$(expr $_interface - 1)]} down
    sleep 1
    macchanger -r ${_interfaces[$(expr $_interface - 1)]}
    sleep 1
    ip link set ${_interfaces[$(expr $_interface - 1)]} up
    exit 0
elif [[ $_choice == manual ]]
then
    echo -n "Please enter a valid MAC address: "
    read -r _mac
    ip link set ${_interfaces[$(expr $_interface - 1)]} down
    sleep 1
    macchanger -m $_mac ${_interfaces[$(expr $_interface - 1)]}
    sleep 1
    ip link set ${_interfaces[$(expr $_interface - 1)]} up
    exit 0
else
    echo "You need to enter \"manual\" or \"random\"!"
    exit 1
fi
