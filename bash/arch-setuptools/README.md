# !WORK IN PROGRESS!
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
bash 000_base.sh new_root (example: sda1)
bash 010_basic_conf_and_grub.sh (no arguments needed, runs in chroot)
bash 020_user_and_sudo.sh (also without arguments, runs on the newly installed system as root)
### Where are we going with this?
If you are installing Arch on over 5 computers (like me) it can get pretty anoying and repettitive pretty quickly. This set of scripts is not for completely automating the install process but to make it easier and much quicker.