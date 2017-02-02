# CERN-alias

# setup

The script `setup.sh` sets up a local user area on LXPLUS and installs various programs to this user area. The programs it installs are as follows:

- ranger
- Irssi

Run the script in the following way:

```Bash
source setup.sh
```

# icons

The colours of icons can be changed using a command such as the following (which would change the colour from CERN blue to grey:

```Bash
sed -i 's/#3861aa/#666666/g' *
```

# themes

## Openbox themes

- CERN_blue
- CERN_white

## Numix themes

```Bash
sudo apt-add-repository -y ppa:numix/ppa
sudo apt-get update
sudo apt-get -y install numix-icon-theme
sudo apt-get -y install numix-icon-theme-circle

gsettings set org.gnome.desktop.interface gtk-theme "Numix"
gsettings set org.gnome.desktop.interface icon-theme "Numix-circle"
```
