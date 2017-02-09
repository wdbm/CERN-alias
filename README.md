# CERN-alias

# setup

The script `setup.sh` sets up a local user area on LXPLUS and installs various programs to this user area. The programs it installs are as follows:

- ranger
- Irssi

Run the script in the following way:

```Bash
source setup.sh
```

# Ubuntu shortkeys and Unity launchers

Ubuntu shortkeys can be set in ways like the following:

```Bash
set_Ubuntu_shortkey.py                                                                 \
    --command="bash -c \"xvkbd -text \$(date \"+%Y-%m-%dT%H%MZ\" --utc) 2>/dev/null\"" \
    --name="type_time_UTC"                                                             \
    --keys="<Control><Shift>d"

set_Ubuntu_shortkey.py         \
    --command="xcalib -i -a"   \
    --name="negative"          \
    --keys="<Control><Shift>m"

set_Ubuntu_shortkey.py         \
    --command="xtrlock"        \
    --name="xtrlock"           \
    --keys="<Control><Shift>l"

set_Ubuntu_shortkey.py                                \
    --command="gnome-terminal --window --full-screen" \
    --name="terminal_fullscreen"                      \
    --keys="<Control><Shift>x"
```

Unity launchers can be set in ways like the following:

```Bash
sleep 0.5
set_Unity7_launcher.py --addlauncher --launcherfile=/usr/share/ucom/CERN-alias/launchers/ATLAS_meetings.desktop
sleep 0.5
set_Unity7_launcher.py --addlauncher --launcherfile=/usr/share/ucom/CERN-alias/launchers/terminal.desktop
sleep 0.5
set_Unity7_launcher.py --addlauncher --launcherfile=/usr/share/ucom/CERN-alias/launchers/Chromium.desktop
sleep 0.5
set_Unity7_launcher.py --addlauncher --launcherfile=/usr/share/ucom/CERN-alias/launchers/Nautilus.desktop
sleep 0.5
set_Unity7_launcher.py --addlauncher --launcherfile=/usr/share/ucom/CERN-alias/launchers/Geany.desktop
sleep 0.5
set_Unity7_launcher.py --addlauncher --launcherfile=/usr/share/ucom/CERN-alias/launchers/screenshot.desktop
sleep 0.5
set_Unity7_launcher.py --addlauncher --launcherfile=/usr/share/ucom/CERN-alias/launchers/color_night.desktop
sleep 0.5
set_Unity7_launcher.py --addlauncher --launcherfile=/usr/share/ucom/CERN-alias/launchers/color_red.desktop
sleep 0.5
set_Unity7_launcher.py --addlauncher --launcherfile=/usr/share/ucom/CERN-alias/launchers/color_normal.desktop
sleep 0.5
set_Unity7_launcher.py --addlauncher --launcherfile=/usr/share/ucom/CERN-alias/launchers/Firefox.desktop
sleep 0.5
set_Unity7_launcher.py --addlauncher --launcherfile=/usr/share/ucom/CERN-alias/launchers/Thunderbird.desktop
sleep 0.5
set_Unity7_launcher.py --addlauncher --launcherfile=/usr/share/ucom/CERN-alias/launchers/download_media.desktop
sleep 0.5
set_Unity7_launcher.py --addlauncher --launcherfile=/usr/share/ucom/CERN-alias/launchers/AirVPN.desktop
sleep 0.5
```

# icons

The colours of icons can be changed using a command such as the following (which would change the colour from CERN blue to grey):

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
