- launchers
    - ATLAS_meetings
        - command: /usr/bin/google-chrome http://cern.ch/go/PM9N
        - icon: /usr/share/ucom/CERN-alias/icons/ATLAS.svg
    - Chrome
        - command: google-chrome
        - icon: /usr/share/ucom/CERN-alias/icons/Chrome.svg
    - Nautilus
        - command: nautilus --no-desktop
        - icon: /usr/share/ucom/CERN-alias/icons/file.svg
    - ranger
        - command: gnome-terminal -x ranger
        - icon: /usr/share/ucom/CERN-alias/icons/gears.svg
    - terminal
        - command: gnome-terminal
        - icon: /usr/share/ucom/CERN-alias/icons/terminal.svg
    - Geany
        - command: geany
        - icon: /usr/share/ucom/CERN-alias/icons/Geany.svg
    - screenshot
        - command: gnome-screenshot --interactive
        - icon: /usr/share/ucom/CERN-alias/icons/camera.svg
    - Thunderbird
        - command: thunderbird %u
        - icon: /usr/share/ucom/CERN-alias/icons/Thunderbird.svg
    - spin
        - command: python spin.py
        - icon: /usr/share/ucom/CERN-alias/icons/spin.svg
    - Xournal
        - command: xournal
        - icon: /usr/share/ucom/CERN-alias/icons/notes.svg
    - Screen Keyboard
        - command: gsettings set org.gnome.desktop.a11y.applications screen-keyboard-enabled true
        - icon: /usr/share/ucom/CERN-alias/icons/keyboard.svg
    - Skype_setup
        - command: bash -c "/usr/bin/skype & /usr/bin/skype-call-recorder"
        - icon: /usr/share/ucom/CERN-alias/icons/Skype.svg
    - VidyoDesktop
        - command: VidyoDesktop
        - icon: /usr/share/ucom/CERN-alias/icons/Vidyo.svg
    - download_media
        - command: python2 /usr/share/pyshared/youtube_dl_gui/__main__.py
        - icon: /usr/share/ucom/CERN-alias/icons/arrow_down.svg
    - calendar
        - command: /usr/bin/google-chrome https://www.google.com/calendar
        - icon: /usr/share/ucom/CERN-alias/icons/time.svg
    - color_night
        - command: bash -c "redshift -o -t 5000:5000 -l 0.0:0.0 &> /dev/null"
        - icon: /usr/share/ucom/CERN-alias/icons/eye.svg
    - color_red
        - command: bash -c "redshift -o -t 1000:1000 -l 0.0:0.0 &> /dev/null"
        - icon: /usr/share/ucom/CERN-alias/icons/eye.svg
    - color_normal
        - command: bash -c "redshift -x &> /dev/null"
        - icon: /usr/share/ucom/CERN-alias/icons/eye.svg
    - Firefox
        - command: firefox %u
        - icon: Icon=/usr/share/ucom/CERN-alias/icons/Firefox.svg
    - unmount_all
        - command: truecrypt -d
        - icon: /usr/share/ucom/CERN-alias/icons/lock.svg
    - xtrlock
        - command: xtrlock
        - icon: /usr/share/ucom/CERN-alias/icons/lock.svg
