#!/bin/bash

################################################################################
#                                                                              #
# setup                                                                        #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This is a setup script.                                                      #
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
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for    #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

name="setup"
version="2017-02-02T1516Z"

echo "setup start"

# Create a local area.
directoryname_local="local"
directoryname_temporary="tmp"
LOCAL="/afs/cern.ch/user/"$(echo "${USER}" | head -c 1)"/"${USER}"/"${directoryname_local}""
echo "create local area "${LOCAL}""
mkdir -p "${LOCAL}"
echo "create temporary area"
mkdir -p ~/"${directoryname_temporary}"
# Set up the PATH.
PATH="${LOCAL}"/usr/bin:"${LOCAL}"/bin:"${PATH}"
# Add the PATH to .bashrc.
echo "add local area to .bashrc"
export PATH="${LOCAL}"/usr/bin:"${LOCAL}"/bin:"${PATH}"
echo "export PATH="${LOCAL}"/usr/bin:"${LOCAL}"/bin:\"\${PATH}\"" >> ~/.bashrc

# Install IRC client Irssi.
cd ~/"${directoryname_temporary}"
echo "install IRC client Irssi"
wget http://www.irssi.org/files/irssi-0.8.17.tar.gz
tar -xvf irssi-0.8.17.tar.gz
cd irssi-0.8.17
./configure --prefix="${LOCAL}"
make
make install

# Install ranger Python module.
pip install --root="${LOCAL}" ranger
#pip install --user ranger
# Install ranger executable.
cd ~/"${directoryname_temporary}"
echo "install ranger"
wget http://nongnu.org/ranger/ranger-stable.tar.gz
tar xvf ranger-stable.tar.gz
cd ranger-*
make install DESTDIR="${LOCAL}"

# Clean up.
cd
echo "remove temporary area"
rm -rf ~/"${directoryname_temporary}"

echo "setup complete"
