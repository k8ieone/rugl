#!/bin/bash

# This will take you the rest of the way.
# It will create a swap file, generate a ssh key, install and configure ZSH, 
# add you to some groups, instal toilet, neofetch, netdata, boinc, yay and powerpill, more netdata stats (boinc, hddtemp, smartd, sensors)
# When this script finishes running, the machine will be configured to my standards. 

# Colors
red=$(tput setaf 1)
green=$(tput setaf 2)
reset=$(tput sgr0)

# Ask about SWAP and set it up

# Install some packages
sudo pacman -S boinc-nox zsh make gcc gc automake autoconf pkg-conf fakeroot binutils netdata openssh hddtemp smartmontools lm_sensors neofetch

echo "Your new SSH private and public key will be generated now..."
ssh-keygen

# Add you to these groups
sudo gpasswd -a $USER dbus
sudo gpasswd -a $USER audio
sudo gpasswd -a $USER video
sudo gpasswd -a $USER wheel
sudo gpasswd -a $USER boinc
sudo gpasswd -a $USER optical
sudo gpasswd -a $USER lp

sudo systemctl enable netdata boinc-client sshd hddtemp smartd

# Additional netdata charts
sudo gpasswd -a netdata boinc
# TODO: get BOINC's gui-rpc value and write it to netdata config
echo "SMARTD_ARGS=\"-A /var/log/smartd/ -i 600\"" | sudo tee /etc/default/smartmontools
sudo mkdir -p /var/log/smartd

echo "Do you wish to run sensors-detect?"
read -r _SENSORS_TRUE
if [[ $_SENSORS_TRUE == y* ]]
then
    sudo sensors-detect
else
    :
fi

# ZSH stuff
echo
echo "${red}WARNING!${reset} An external script will now be run! Is this OK?"
echo "y/N: "
read _OK
if [[ $_OK == y* ]]
then
    sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
    git clone https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/custom/themes/powerlevel10k
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
    git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
    mv ~/rugl/bash/arch-setuptools/configs/user/zshrc ~/.zshrc
else
    echo "ZSH setup will be skipped!"
fi

# Install yay and powerpill
cd ~
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ..
sudo rm -r yay
yay -S powerpill toilet

echo
echo "${green}Done!${reset}"
echo "My customisations are done!"
echo
