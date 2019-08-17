#!/bin/bash

#-------------------------------------------------------------
# UNLESS YOU WANT TO BREAK YOUR SYSTEM DO NOT RUN THIS SCRIPT
#-------------------------------------------------------------

# Usage: bash 00_base.sh partition (ex. sda1)
# set -e # This auto exits the script if any command returns a non-zero value

# COLORS
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

# Check internet access

wget -q --spider https://archlinux.org
if [ $? -eq 0 ]
then
    :
else
    echo "${red}Internet connection not available"
    echo "Aborting..."
    exit 1
fi

# Check if partition exists

fdisk -l /dev/$1
if [ $? -eq 0 ]
then
    :
else
    echo "${red}Partition $1 not found"
    echo "Aborting..."
    exit 1
fi

# Check boot mode

if [ -d /sys/firmware/efi/efivars ]
then
    _BOOTMODE=EFI
    echo -n "Please specify the EFI system partition:"
    read _EFIPART
else
    _BOOTMODE=BIOS
fi

# Now we enable NTP

echo Let\'s set the correct time
timedatectl set-ntp true

# Format and mount root
echo "${red}WARNING"
echo "$1 will be formated as ext4 and used as root"
echo "Is this OK?"
read _OK
if  [[ $_OK == y* ]]
then
    :
elif [[ $_OK == n* ]]
then
    echo "Aborted by user"
    exit 1
else
    echo "That was a yes or no question..."
    exit 1
fi

mkfs.ext4 /dev/$1
sleep 2
mount /dev/$1 /mnt

# Here we format and mount the EFI partition

if [ $_BOOTMODE == EFI]
then
    echo "${red}WARNING"
    echo "$_EFIPART will be formated as FAT32"
    echo "If you answer no the partition will be left untouched"
    read _OK
    if  [[ $_OK == y* ]]
    then
        echo "Formating EFI partition /dev/$_EFIPART"
        mkfs.fat -F32 /dev/$_EFIPART
        sleep 2
        mount /dev/$_EFIPART /mnt/boot
    elif [[ $_OK == n* ]]
    then
        echo "Skipping formating /dev/$_EFIPART"
        mount /dev/$_EFIPART /mnt/boot
    else
        echo "Aborting..."
        exit 1
    fi
fi

# Installing the base packages
pacstrap /mnt base

# Generating fstab
genfstab -U /mnt >> /mnt/etc/fstab
cat /mnt/etc/fstab

echo
echo "${green}Installation finished"
echo "Brief summary of what was done:"
echo "1. Formated root as ext4"
if [[ $_OK == y* ]]
then
    echo "1.5. Formated EFI system partition as FAT32"
else
    :
fi
echo "2. installed the base package group to root"
echo "3. Generated a fstab"
echo
exit 0
# Todo: delete the directory after the script finishes and clone it to the chroot
