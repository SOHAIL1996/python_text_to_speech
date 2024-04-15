#!/usr/bin/env bash

# Software License Agreement (BSD)
#
# @author    Salman Omar Sohail <sorox23@gmail.com>
# @copyright (c) 2024, Salman Omar Sohail, Inc., All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of Salman Omar Sohail nor the names of its contributors
#   may be used to endorse or promote products derived from this software
#   without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Redistribution and use in source and binary forms, with or without
# modification, is not permitted without the express permission
# of Salman Omar Sohail.

function color_echo () {
    echo "$(tput setaf 1)$1$(tput sgr0)"
}

function install_ros2_dependencies () {
    color_echo "Installing build pacakges."
    sudo apt-get install python3 \
                         python3-colcon-common-extensions \
                         python3-flake8 \
                         python3-pip \
                         python3-pytest-cov \
                         python3-setuptools \
                         python3-vcstool \
                         espeak-ng \
                         wget -y

    color_echo "Installed Python3 build pacakges."
}

function install_pip_packages () {
    color_echo "Installing pip pacakges."
    pip install TTS pygame -y
}

function install_ros2_ur_packages () {
    color_echo "Installing build pacakges."
    sudo apt-get install ros-humble-moveit-*\
                         ros-humble-moveit-servo\
                         ros-humble-ur-* -y
}

function prompt_yes_no() {
    while true; do
        read -p "$1 (y/n): " yn
        case $yn in
            [Yy]* ) return 0;;  # Return 0 for Yes
            [Nn]* ) return 1;;  # Return 1 for No
            * ) echo "Please answer yes or no.";;
        esac
    done
}

RED='\033[0;31m'
DGREEN='\033[0;32m'
GREEN='\033[1;32m'
WHITE='\033[0;37m'
BLUE='\033[1;34m'
CYAN='\033[1;36m'
NC='\033[0m' 
                  
echo -e "----------------------------------------------------------"                                                                        
echo -e "${DGREEN}"
echo -e "███████╗ ██████╗ ██████╗  ██████╗ ██╗  ██╗██████╗ ██████╗ "
echo -e "██╔════╝██╔═══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚════██╗╚════██╗"
echo -e "███████╗██║   ██║██████╔╝██║   ██║ ╚███╔╝  █████╔╝ █████╔╝"
echo -e "╚════██║██║   ██║██╔══██╗██║   ██║ ██╔██╗ ██╔═══╝  ╚═══██╗"
echo -e "███████║╚██████╔╝██║  ██║╚██████╔╝██╔╝ ██╗███████╗██████╔╝"
echo -e "╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ "
echo -e "----------------------------------------------------------"
echo -e "Installing Required Libraries and dependencies!   "                                                                                                                                         
echo -e "----------------------------------------------------------${NC}"

install_ros2_dependencies
install_pip_packages

# if prompt_yes_no "Do you want to install ROS2 Universal Robot packages?"; then
#     install_ros2_ur_packages
# fi

echo "Installation complete."