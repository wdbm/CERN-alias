#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# change_colours.py                                                            #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program changes the colors of icons in the working directory and the    #
# colors defined in itself.                                                    #
#                                                                              #
# copyright (C) 2015 William Breaden Madden                                    #
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
"""

name    = "change_colors"
version = "2015-04-15T1745Z"

import os

def main():

    _color_1 = "#000000"
    _color_2 = "#3861aa"

    color_1 = raw_input(
        "The value of color 1 is {color_1}.\nEnter the new value for color 1 in"
        " hex triplet form prepended by \"#\": ".format(
            color_1 = _color_1
        )
    )
    print(
        "The value of color 1 has been set to {color_1}.".format(
            color_1 = color_1
        )
    )
    color_2 = raw_input(
        "The value of color 2 is {color_2}.\nEnter the new value for color 2 in"
        " hex triplet form prepended by \"#\": ".format(
            color_2 = _color_2
        )
    )
    print(
        "The value of color 2 has been set to {color_2}.".format(
            color_2 = color_2
        )
    )
    os.system("sed -i \'s/" + _color_1 + "/" + color_1 + "/g\' *.svg *.py")
    os.system("sed -i \'s/" + _color_2 + "/" + color_2 + "/g\' *.svg *.py")

if __name__ == "__main__":
    main()
