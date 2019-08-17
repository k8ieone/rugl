# README NOT UP TO DATE!
### Badges
![GitHub issues by-label](https://img.shields.io/github/issues-raw/satcom886/rugl/arch-setuptools.svg)
### What can I do with this?
This is a set of bash scripts that will help you deploy Arch Linux.
### Is it ready?
The first script (00_base.sh) is ready.
### What does each script do?
00_base.sh - Formats the root partition (+efi partition) and installs the base package group. It leaves you with an installed system that is ready to chroot into (basically everything up to the "Chroot" section of the install guide)
### Usage:
bash 00_base.sh new_root (example: sda1)
### Where are we going with this?
If you are installing Arch on over 5 computers (like me) it can get pretty anoying and repettitive pretty quickly. This set of scripts is not for completely automating the install process but to make it easier and much quicker.