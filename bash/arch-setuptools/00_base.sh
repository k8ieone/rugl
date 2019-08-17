#!/bin/bash

#-------------------------------------------------------------
# UNLESS YOU WANT TO BREAK YOUR SYSTEM DO NOT RUN THIS SCRIPT
#-------------------------------------------------------------

# Usage: bash 00_base.sh partition (ex. sda1)

echo Make sure the network works and you have internet access
# todo: Check internet access
echo Please partition the desired drive to your liking and specify the future root partition as the first parameter
# todo: Check if the first parameter is a valid partition

if [ -d /sys/firmware/efi/efivars ]
then
    echo You are running EFI
    _BOOTMODE=EFI
    # todo: make a variable that contains the efi system partition
    # This bootmode is unsupported for now
    # In order to install GRUB run this command: grub-install ...
else
    echo You are running a traditional BIOS
    _BOOTMODE=BIOS
fi

echo Let\'s set the correct time
timedatectl set-ntp true
