#!/bin/bash

# Usage: bash 00_base.sh partition (ex. sda1)

# COLORS
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

# Check if partition exists
if fdisk -l /dev/$1
then
    :
else
    echo
    echo "${red}Partition $1 not found${reset}"
    echo "Aborting..."
    exit 1
fi

# Check boot mode
if [ -d /sys/firmware/efi/efivars ]
then
    _BOOTMODE=EFI
    echo
    echo -n "Please specify the EFI system partition: /dev/"
    read -r _EFIPART
else
    _BOOTMODE=BIOS
fi

# Now we enable NTP
echo Let\'s set the correct time
timedatectl set-ntp true

# Format and mount root
echo
echo "${red}WARNING${reset} $1 will be formated as ext4 and used as root"
echo -n "Is this OK? "
read -r _OK
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
if [[ $_BOOTMODE == EFI ]]
then
    echo
    echo "${red}WARNING${reset}"
    echo "$_EFIPART will be formated as FAT32"
    echo "If you answer no the partition will be left untouched"
    echo -n "y/n "
    read -r _OK
    if  [[ $_OK == y* ]]
    then
        echo "Formating EFI partition /dev/$_EFIPART"
        mkfs.fat -F32 /dev/$_EFIPART
        sleep 2
        mkdir /mnt/boot
        mount /dev/$_EFIPART /mnt/boot
    elif [[ $_OK == n* ]]
    then
        echo "Skipping formating /dev/$_EFIPART"
        mkdir /mnt/boot
        mount /dev/$_EFIPART /mnt/boot
    else
        echo "Aborting..."
        exit 1
    fi
fi

# Installing the base packages
pacstrap /mnt base linux linux-firmware

# Generating fstab
genfstab -U /mnt >> /mnt/etc/fstab
cat /mnt/etc/fstab

# Run the script that sets up this repo inside the chroot
cd ~
cp rugl/bash/arch-setuptools/001_do_not_run.sh /mnt
arch-chroot /mnt bash /001_do_not_run.sh
rm -r rugl

echo
echo "${green}Installation finished!${reset}"
echo "Brief summary of what was done:"
echo "1. Formated root as ext4"
if [[ $_OK == y* ]] && [[ $_BOOTMODE == EFI ]]
then
    echo "1.5. Formated EFI system partition as FAT32"
else
    :
fi
echo "2. installed the base package group to root"
echo "3. Generated a fstab"
echo "4. Installed git and cloned this repo into the chroot"
echo "The next step would be to chroot into /mnt and start 010"
echo
exit 0
