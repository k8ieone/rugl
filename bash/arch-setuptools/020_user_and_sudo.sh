#!/bin/bash

# This will just create a user and add it to /etc/sudoers
# Also install sudo and remove this repo from this directory
# and clone it into the new user's home (make sure the user owns the directory)
# Maybe I should enable NTP again?

# Colors
red=$(tput setaf 1)
green=$(tput setaf 2)
reset=$(tput sgr0)

# Enable NTP again
timedatectl set-ntp true

pacman -S sudo

# What will be your username
echo -n "Enter your new username: "
read -r _USERNAME

# Create the user
useradd -m $_USERNAME
passwd $_USERNAME

# Add you to sudoers
echo "$_USERNAME ALL=(ALL) ALL" >> /etc/sudoers
echo "Defaults:$_USERNAME      !authenticate" >> /etc/sudoers

# Clone to the new user's home directory
cd /home/$_USERNAME
git clone https://github.com/satcom886/rugl
chown -R $_USERNAME:$_USERNAME rugl
rm -r /root/rugl

echo
echo "${green}Done!${reset}"
echo "Summary:"
echo "1. Created the user $_USERNAME and added it to sudoers"
echo "2. Cloned this repo to $_USERNAME's home directory"
echo "You can now login as $_USERNAME and proceed with customisations from there."
echo
