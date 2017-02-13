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
    --clearlaunchers         clear current launchers
    --debugpassive           display commands without executing
"""

name    = "set_Unity7_launcher"
version = "2017-02-13T1408Z"
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
    clear_launchers   = options["--clearlaunchers"]
    debug_passive     = options["--debugpassive"]
    if filename_launcher is None and\
        not inspect_launchers and\
        not clear_launchers:
        print("no launcher file specified")
        exit()

    launchers_current = subprocess.check_output([
                            "gsettings",
                            "get",
                            "com.canonical.Unity.Launcher",
                            "favorites"
                        ]).decode("utf-8")
    launchers_current = eval(launchers_current)
    if not inspect_launchers and not clear_launchers:
        filepath_launcher = os.path.dirname(os.path.abspath(filename_launcher))
        filename_launcher = os.path.split(filename_launcher)[-1]
        launcher_applications =\
            [index for index, launcher in enumerate(launchers_current) if\
            launcher.startswith("application://")]
        if launcher_applications:
            index_launcher_new = launcher_applications[-1]
        else:
            index_launcher_new = 0
        new_launcher =\
            "application://" + filepath_launcher + "/" + filename_launcher
        if add_launcher:
            if not new_launcher in launchers_current:
                print("add launcher {launcher}".format(
                    launcher = new_launcher
                ))
                launchers_current.insert(index_launcher_new, new_launcher)
                command_list = [
                    "gsettings",
                    "set",
                    "com.canonical.Unity.Launcher",
                    "favorites",
                    str(launchers_current)
                ]
                if debug_passive:
                    print(" ".join(command_list))
                else:
                    subprocess.Popen(command_list)
            else:
                print("launcher already present")
                exit()
        elif remove_launcher:
            launchers_current.remove(new_launcher)
            command_list = [
                "gsettings",
                "set",
                "com.canonical.Unity.Launcher",
                "favorites",
                str(launchers_current)
            ]
            if debug_passive:
                print(" ".join(command_list))
            else:
                subprocess.Popen(command_list)
    elif inspect_launchers:
        print("\ncurrent launchers:\n")
        for launcher in launchers_current:
            print(launcher)
        print("")
    elif clear_launchers:
        launchers_clear =\
            [launcher for launcher in launchers_current if\
            not launcher.startswith("application://")]
        command_list = [
            "gsettings",
            "set",
            "com.canonical.Unity.Launcher",
            "favorites",
            str(launchers_clear)
        ]
        if debug_passive:
            print(" ".join(command_list))
        else:
            subprocess.Popen(command_list)

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
