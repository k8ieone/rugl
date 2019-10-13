#!/bin/bash

# This script shoould be run as the new user. It will just setup some basic configs + zsh

# Colors
red=$(tput setaf 1)
green=$(tput setaf 2)
reset=$(tput sgr0)

# GTK Theme
mkdir -p .config/gtk-3.0
rm ~/.config/gtk-3.0/settings.ini
cp ~/rugl/bash/arch-setuptools/configs/user/gtk3.ini ~/.config/gtk-3.0/settings.ini
# Configure i3
rm ~/config/i3/config
mkdir -p .config/i3
cp ~/rugl/bash/arch-setuptools/configs/user/i3.conf ~/.config/i3/config
# Configure i3cat
mkdir -p ~/.i3
cp ~/rugl/bash/arch-setuptools/configs/user/i3cat.conf ~/.i3/
cp ~/rugl/bash/arch-setuptools/configs/user/exit_script.sh ~/.i3/
cp ~/rugl/bash/arch-setuptools/configs/user/mpd-nowplaying.sh ~/.i3/
# Configure MPD
mkdir -p ~/.config/mpd
mkdir ~/.config/mpd/playlists
mkdir ~/Music
cp ~/rugl/bash/arch-setuptools/configs/user/mpd.conf ~/.config/mpd/
# Redshift config
cp ~/rugl/bash/arch-setuptools/configs/user/redshift.conf ~/.config/

# Generate SSH keys
echo "Your new SSH private and public key will be generated now..."
ssh-keygen

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
