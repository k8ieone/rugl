#!/bin/bash

# Finall install script that will install i3 along with my configs and some basic utilities

# Colors
red=$(tput setaf 1)
green=$(tput setaf 2)
reset=$(tput sgr0)

# Ask about SWAP and set it up
echo "Do you wish to setup a SWAP file?"
echo -n "y/N: "
read -r _SWAP
if [[ $_SWAP == y* ]]
then
    sudo fallocate -l 2048M /swapfile
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile
    echo "/swapfile none swap defaults 0 0" | sudo tee -a /etc/fstab
else
    :
fi

# Install basic packages
sudo pacman -S boinc zsh make gcc gc automake autoconf pkgconf fakeroot binutils netdata hddtemp smartmontools lm_sensors neofetch rng-tools opensc systemd-swap

# Install yay and powerpill
cd ~
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ~
sudo rm -r yay
yay -S powerpill toilet

# Install Xorg, i3 and some stuff
sudo pacman -S xorg dmenu i3-gaps i3status xorg-xinit adapta-gtk-theme mpd scrot redshift network-manager-applet bluez bluez-utils blueman terminator ttf-ubuntu-font-family pulseaudio pulseaudio-alsa pulseaudio-bluetooth pulseaudio-zeroconf paprefs pavucontrol arandr
yay -S i3lock-fancy-git paper-icon-theme-git i3cat-git twmnd-git indicator-powersave

# Setup i3 configs
mkdir -p .config/twmn
cp ~/rugl/bash/arch-setuptools/configs/user/twmn.conf ~/.config/twmn/twmn.conf
mkdir -p .config/gtk-3.0
rm ~/.config/gtk-3.0/settings.ini
cp ~/rugl/bash/arch-setuptools/configs/user/gtk3.ini ~/.config/gtk-3.0/settings.ini
rm ~/config/i3/config
mkdir -p .config/i3
cp ~/rugl/bash/arch-setuptools/configs/user/i3.conf ~/.config/i3/config
mkdir -p ~/.i3
cp ~/rugl/bash/arch-setuptools/configs/user/i3cat.conf ~/.i3/
cp ~/rugl/bash/arch-setuptools/configs/user/exit_script.sh ~/.i3/
cp ~/rugl/bash/arch-setuptools/configs/user/mpd-nowplaying.sh ~/.i3/
sudo mv ~/rugl/bash/arch-setuptools/configs/system-wide/30-touchpad.conf /etc/X11/xorg.conf.d/
mkdir -p ~/.config/mpd
cp ~/rugl/bash/arch-setuptools/configs/user/mpd.conf ~/.conf/mpd

# Generate SSH keys
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

sudo systemctl enable netdata boinc-client hddtemp smartd rngd bluetooth

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
echo -n "y/N: "
read -r _OK
if [[ $_OK == y* ]]
then
    echo "${red}WARNING!${reset}"
    echo "The following script will drop you to ZSH, be sure to type \"exit\" to continue the script."
    sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
    git clone https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/custom/themes/powerlevel10k
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
    git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
    echo "export ZSH=\"/home/$USER/.oh-my-zsh\"" > ~/.zshrc
    cat ~/rugl/bash/arch-setuptools/configs/user/zshrc | tee -a ~/.zshrc
    # Setup xinit
    rm .xinitrc .zprofile
    cp ~/rugl/bash/arch-setuptools/configs/user/xinitrc ~/.xinitrc
    cp ~/rugl/bash/arch-setuptools/configs/user/zprofile ~/.zprofile
else
    echo "ZSH setup will be skipped!"
    echo "${red}Warning! ${reset}i3 will not start because of ZSH missing!"
    echo "You will have to start it manually using startx!"
fi
