#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# set_Ubuntu_shortkey                                                          #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program sets an ubuntu shortkey.                                        #
#                                                                              #
# copyright (C) 2017 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

usage:
    program [options]

options:
    -h, --help               display help message
    --version                display version and exit
    -v, --verbose            verbose logging
    -s, --silent             silent
    -u, --username=USERNAME  username
    --command=TEXT           command
    --keys=TEXT              keys
    --name=TEXT              name
"""

name    = "set_Ubuntu_shortkey"
version = "2017-02-09T1943Z"
logo    = None

import docopt
import logging
import os
import subprocess
import sys
import time

def main(options):

    command = options["--command"]
    keys    = options["--keys"]
    name    = options["--name"]

    if any([command, keys, name]) is None:
        print("insufficient options specified")
        exit()

    print("\nset shortkey:"          )
    print("- name:    " + name       )
    print("- command: " + command    )
    print("- keys:    " + keys + "\n")

    shortkeys_current     = subprocess.check_output([
                               "gsettings",
                               "get",
                               "org.gnome.settings-daemon.plugins.media-keys",
                               "custom-keybindings"
                           ]).decode("utf-8")
    if shortkeys_current.strip() == "@as []":
        shortkeys_current = "[]"
    shortkeys_current     = eval(shortkeys_current)
    index_shortkey_new    = len(shortkeys_current)
    address_shortkey_new  =\
        "/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/" +\
        "custom" + str(index_shortkey_new) + "/"
    shortkeys_current.append(
        address_shortkey_new
    )

    subprocess.Popen([
        "gsettings",
        "set",
        "org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:" +\
            address_shortkey_new,
        "name",
        name
    ])

    subprocess.Popen([
        "gsettings",
        "set",
        "org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:" +\
            address_shortkey_new,
        "command",
        command
    ])

    subprocess.Popen([
        "gsettings",
        "set",
        "org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:" +\
            address_shortkey_new,
        "binding",
        keys
    ])

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
