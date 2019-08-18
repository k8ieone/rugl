#!/bin/bash
# Everything in the install guide (from the chroot step) and installs some of my configs
# (grub, pacman [ONLY AFTER PACSERVE IS SETUP, maybe create a temporary copy without pacserve?], vconsole.conf, locale.conf, hosts)

# COLORS
red=$(tput setaf 1)
green=$(tput setaf 2)
reset=$(tput sgr0)

echo "WARNING! This script should be run in the /mnt chroot as root (not with sudo)!"

# Check internet access again
wget -q --spider https://archlinux.org
if [ $? -eq 0 ]
then
    :
else
    echo
    echo "${red}Internet connection not available${reset}"
    echo "Aborting..."
    exit 1
fi

# Check boot mode again
if [ -d /sys/firmware/efi/efivars ]
then
    _BOOTMODE=EFI
else
    _BOOTMODE=BIOS
fi

echo "Enter your desired hostname: "
read -r _HOSTNAME

# This is where I'm getting too lazy to make this an argument so I'm hardcoding the timezone
ln -sf /usr/share/zoneinfo/Europe/Prague /etc/localtime
sleep 1
hwclock --systohc

# Uncomment the locales in /etc/locales.gen
# Seems like I'm hardcoding everything...
sed -i '/^#.* cs_CZ.UTF-8 /s/^#//' /etc/locale.gen
sed -i '/^#.* en_US.UTF-8 /s/^#//' /etc/locale.gen

# Locale configuration
echo "LOCALE=cs_CZ.UTF-8" > /etc/locale.conf
echo "LANG=en_US.UTF-8" >> /etc/locale.conf
echo "KEYMAP=cz-qwertz" > /etc/vconsole.conf

# Hostname configuration
echo $_HOSTNAME > /etc/hostname
echo "127.0.0.1	localhost" >> /etc/hosts
echo "::1		localhost" >> /etc/hosts
echo "127.0.1.1	$_HOSTNAME.local	$_HOSTNAME" >> /etc/hosts

# Root password
loadkeys cz-qwertz
echo "You will now be prompted to enter your new root password"
echo "Keyboard layout: cz-qwertz"
passwd

# Install GRUB
# TODO: Figure out SWAP in order to allow for suspend to disk
if [[ $_BOOTMODE == BIOS ]]
then
    pacman -S grub
    echo
    echo -n "Please enter the destination disk (not partition): "
    read -r _INSTALLDISK
    grub-install --target=i386-pc /dev/$_INSTALLDISK
    cp configs/system-wide/grub /etc/default/grub
    grub-mkconfig -o /boot/grub/grub.cfg
elif [[ $_BOOTMODE == EFI ]]
then
    pacman -S grub efibootmgr
    grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=Arch
    cp configs/system-wide/grub /etc/default/grub
    grub-mkconfig -o /boot/grub/grub.cfg
fi

# Install NetworkManager and OpenSSH
pacman -S networkmanager openssh
systemctl enable NetworkManager
systemctl enable sshd.service

echo
echo "${green}Success! ${reset}GRUB is now installed and some of the basic system settings are set!"
echo "Summary:"
echo "1. Installed GRUB, NetworkManager, OpenSSH server"
echo "2. Configured keyboard layout, language, locale and hostname"
echo "After a reboot you can start configuring the system to your liking!"
echo
