#!/bin/bash

# Colors
red=$(tput setaf 1)
green=$(tput setaf 2)
reset=$(tput sgr0)

# Check internet access
if wget -q --spider https://archlinux.org
then
    :
else
    echo
    echo "${red}Internet connection not available${reset} or archlinux.org website is down"
    echo "Aborting..."
    exit 1
fi

# Now we enable NTP
echo Let\'s set the correct time
timedatectl set-ntp true

echo "Enter your desired hostname: "
read -r _HOSTNAME

# This is where I'm getting too lazy to make this an argument so I'm hardcoding the timezone
ln -sf /usr/share/zoneinfo/Europe/Prague /etc/localtime
sleep 1
hwclock --systohc

# Uncomment the locales in /etc/locales.gen
# Seems like I'm hardcoding everything...
sed -i '/^#.*en_US.UTF-8 /s/^#//' /etc/locale.gen
sed -i '/^#.*cs_CZ.UTF-8 /s/^#//' /etc/locale.gen

# Locale configuration
echo "LOCALE=cs_CZ.UTF-8" > /etc/locale.conf
echo "LANG=en_US.UTF-8" >> /etc/locale.conf
echo "KEYMAP=cz-qwertz" > /etc/vconsole.conf
locale-gen

# Hostname configuration
echo $_HOSTNAME > /etc/hostname
echo "127.0.0.1	localhost" >> /etc/hosts
echo "::1		localhost" >> /etc/hosts
echo "127.0.1.1	$_HOSTNAME.local	$_HOSTNAME" >> /etc/hosts

# Enable multicore compiling in makepkg.conf
sed -i '/ MAKEFLAGS /s/^/#/' /etc/makepkg.conf
echo "MAKEFLAGS=\"-j\$(nproc)\"" >> /etc/makepkg.conf

# Root password
loadkeys cz-qwertz
echo "You will now be prompted to enter your new root password"
echo "Keyboard layout: cz-qwertz"
passwd

pacman -S networkmanager
systemctl enable NetworkManager

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
