#!/usr/bin/env python3

"""
################################################################################
#                                                                              #
# set_Unity7_launcher                                                          #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program sets a Unity7 launcher.                                         #
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
    --launcherfile=FILENAME  launcher filename (.desktop file)
    --addlauncher            add launcher
    --removelauncher         remove launcher
    --inspectlaunchers       inspect current launchers
"""

name    = "set_Unity7_launcher"
version = "2017-02-02T1639Z"
logo    = None

import docopt
import logging
import os
import subprocess
import sys
import time

def main(options):

    filename_launcher = options["--launcherfile"]
    add_launcher      = options["--addlauncher"]
    remove_launcher   = options["--removelauncher"]
    inspect_launchers = options["--inspectlaunchers"]
    if filename_launcher is None and not inspect_launchers:
        print("no launcher file specified")
        exit()

    launchers_current = subprocess.check_output([
                            "gsettings",
                            "get",
                            "com.canonical.Unity.Launcher",
                            "favorites"
                        ]).decode("utf-8")
    launchers_current = eval(launchers_current)
    if not inspect_launchers:
        filepath_launcher = os.path.dirname(os.path.abspath(filename_launcher))
        index_launcher_new =\
            [index for index, launcher in enumerate(launchers_current) if\
            launcher.startswith("application://")][-1] + 1
        new_launcher =\
            "application://" + filepath_launcher + "/" + filename_launcher
        if add_launcher:
            if not new_launcher in launchers_current:
                print("add launcher {launcher}".format(
                    launcher = new_launcher
                ))
                launchers_current.insert(index_launcher_new, new_launcher)
                subprocess.Popen([
                                    "gsettings",
                                    "set",
                                    "com.canonical.Unity.Launcher",
                                    "favorites",
                                    str(launchers_current)
                                ])
            else:
                print("launcher already present")
                exit()
        elif remove_launcher:
            launchers_current.remove(new_launcher)
            subprocess.Popen([
                                "gsettings",
                                "set",
                                "com.canonical.Unity.Launcher",
                                "favorites",
                                str(launchers_current)
                            ])
    else:
        print("\ncurrent launchers:\n")
        for launcher in launchers_current:
            print(launcher)
        print("")

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
