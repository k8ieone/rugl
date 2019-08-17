#!/bin/bash

#-------------------------------------------------------------
# UNLESS YOU WANT TO BREAK YOUR SYSTEM DO NOT RUN THIS SCRIPT
#-------------------------------------------------------------

# Usage: bash 00_base.sh partition (ex. sda1)
# set -e # This auto exits the script if any command returns a non-zero value

# COLORS
#red=`tput setaf 1`
#green=`tput setaf 2`
#reset=`tput sgr0`
# maybe later...

# First we check stuff

echo Making sure the network works and you have internet access...
echo
wget -q --spider https://archlinux.org
if [ $? -eq 0 ]
then
    echo "Network OK"
    echo "Moving on"
    echo
else
    echo "Internet connection not available"
    echo "Aborting..."
    exit 1
fi

echo Please partition the desired disk to your liking and specify the future root partition as the first parameter
echo I recommend using cfdisk
echo
fdisk -l /dev/$1
if [ $? -eq 0 ]
then
    echo "Partition $1 is a valid partition"
    echo "Moving on"
    echo
else
    echo "Partition $1 not found"
    echo "Aborting..."
    exit 1
fi

if [ -d /sys/firmware/efi/efivars ]
then
    echo You are running EFI
    echo "This mode is not supported yet"
    echo
    _BOOTMODE=EFI
    # todo: make a variable that contains the efi system partition
    # In order to install GRUB run this command: grub-install ...
else
    echo You are running a traditional BIOS
    echo
    _BOOTMODE=BIOS
fi


# Now we enable NTP

echo Let\'s set the correct time
timedatectl set-ntp true

# Partition
echo "$1 will be formated as ext4"
echo "Is this OK?"
read OK
if  [[ $OK == y* ]]
then
    echo "Moving on"
elif [[ $OK == n* ]]
then
    echo "That was a no"
    echo "Aborted by user"
    exit 1
else
    echo "That was a yes or no question..."
    exit 1
fi

mkfs.ext4 /dev/$1
echo "SWAP file will not be created"
echo "Create one if you wish"
echo "Visit the wiki for instructions"
echo

echo "Now mounting /dev/$1"
mount /dev/$1 /mnt
# This is where we would format and mount the EFI partition

# Installing the base packages
pacstrap /mnt base

# Generating fstab
genfstab -U /mnt >> /mnt/etc/fstab

echo "Installation finished"
echo "Now you should chroot into the install directory and start creating users"
echo "Also don't forget to install the bootloader"
echo
exit 0
