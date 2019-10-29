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
sudo pacman -S zsh make gcc gc automake patch autoconf pkgconf fakeroot binutils hddtemp smartmontools lm_sensors neofetch rng-tools opensc systemd-swap

# Install yay
cd ~
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ~
sudo rm -r yay

# Install Xorg, i3 and some stuff
sudo pacman -S xorg dmenu xsecurelock i3-gaps notification-daemon mpc i3status xorg-xinit glava ttf-font-awesome adapta-gtk-theme mpd scrot redshift powerline-fonts network-manager-applet bluez bluez-utils blueman terminator ttf-ubuntu-font-family pulseaudio pulseaudio-alsa pulseaudio-bluetooth pulseaudio-zeroconf paprefs pavucontrol arandr
yay -S paper-icon-theme-git i3cat-git indicator-powersave powerpill toilet clight compton-tryone-git

## Configs
# i3status config
sudo mv ~/rugl/bash/arch-setuptools/configs/system-wide/i3status.conf /etc/i3status.conf
# TWMN
#mkdir -p .config/twmn
#cp ~/rugl/bash/arch-setuptools/configs/user/twmn.conf ~/.config/twmn/twmn.conf
# GTK Theme
mkdir -p ~/.config/gtk-3.0
rm ~/.config/gtk-3.0/settings.ini
cp ~/rugl/bash/arch-setuptools/configs/user/gtk3.ini ~/.config/gtk-3.0/settings.ini
# Configure i3
rm ~/.config/i3/config
mkdir -p ~/.config/i3
cp ~/rugl/bash/arch-setuptools/configs/user/i3.conf ~/.config/i3/config
# Configure i3cat
mkdir -p ~/.i3
cp ~/rugl/bash/arch-setuptools/configs/user/i3cat.conf ~/.i3/
cp ~/rugl/bash/arch-setuptools/configs/user/exit_script.sh ~/.i3/
cp ~/rugl/bash/arch-setuptools/configs/user/mpd-nowplaying.sh ~/.i3/
cp ~/rugl/bash/arch-setuptools/configs/user/toggle_clight.sh ~/.i3/
cp ~/rugl/bash/arch-setuptools/configs/user/toggle_compositing.sh ~/.i3/
# Touchpad config
sudo mv ~/rugl/bash/arch-setuptools/configs/system-wide/30-touchpad.conf /etc/X11/xorg.conf.d/
# Configure MPD
mkdir -p ~/.config/mpd
mkdir ~/.config/mpd/playlists
mkdir ~/Music
cp ~/rugl/bash/arch-setuptools/configs/user/mpd.conf ~/.config/mpd/
# Redshift config
cp ~/rugl/bash/arch-setuptools/configs/user/redshift.conf ~/.config/
# Clight config
cp ~/rugl/bash/arch-setuptools/configs/user/clight.conf ~/.config/
# Compton config
cp ~/rugl/bash/arch-setuptools/configs/user/compton.conf ~/.config/

# Generate SSH keys
echo "Your new SSH private and public key will be generated now..."
ssh-keygen

# Add you to these groups
sudo gpasswd -a $USER dbus
sudo gpasswd -a $USER audio
sudo gpasswd -a $USER video
sudo gpasswd -a $USER wheel
sudo gpasswd -a $USER optical
sudo gpasswd -a $USER lp

sudo systemctl enable hddtemp smartd rngd bluetooth

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
    rm ~/.xinitrc ~/.zprofile
    cp ~/rugl/bash/arch-setuptools/configs/user/xinitrc ~/.xinitrc
    cp ~/rugl/bash/arch-setuptools/configs/user/zprofile ~/.zprofile
else
    echo "ZSH setup will be skipped!"
    echo "${red}Warning! ${reset}i3 will not start because of ZSH missing!"
    echo "You will have to start it manually using startx!"
fi
echo "Sidenote: glava will probably have the wrong resolution. Use screen height - 250 - 20 as the window y position and 250 as height."
