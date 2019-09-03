### Badges
![GitHub issues by-label](https://img.shields.io/github/issues-raw/satcom886/rugl/arch-setuptools.svg)
### What can I do with this?
This is a set of bash scripts that will help you deploy Arch Linux.
### Is it ready?
Everything up to 010 works.
### What does each script do?
000_base.sh - Formats the root partition (+efi partition) and installs the base package group. It leaves you with an installed system that is ready to chroot into (basically everything up to the "Chroot" section of the install guide)  
010_basic_conf_and_grub.sh - Sets up the hostname, keyboard layout, locale and istalls GRUB.  
020_user_and_sudo.sh - Creates a new user, makes it the admin and clones this repo to the user's home.  
### Usage:
These are the commands you have to run:
1. ip a (make sure you have an IP address, maybe try to ping something)
1. pacman -Sy
1. pacman -S git
1. git clone https://github.com/satcom886/rugl
1. cfdisk /dev/[YOUR DISK]
1. cd rugl/bash/arch-setuptools
1. bash 000_base.sh [YOUR DISK]
1. arch-chroot /mnt
1. cd root
1. bash rugl/bash/arch-setuptools/010_basic_conf_and_grub.sh
1. exit
1. umount /mnt
1. reboot
1. [LOGIN AS ROOT]
1. bash rugl/bash/arch-setuptools/020_user_and_sudo.sh
1. exit
1. [LOGIN AS USER]
1. bash rugl/bash/arch-setuptools/030_final_tweaks_headless.sh
1. reboot
### Where are we going with this?
If you are installing Arch on over 5 computers (like me) it can get pretty anoying and repettitive pretty quickly. This set of scripts is not for completely automating the install process but to make it easier and much quicker.