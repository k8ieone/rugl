#!/bin/bash

# THIS FILE IS RUN AUTOMATICALLY
# It just installs git and clones this repo into the chroot

cd ~
pacman -S git
git clone https://github.com/satcom886/rugl.git
echo "Hello from the other side"
rm /001_do_not_run.sh
exit 0
