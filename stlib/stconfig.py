#!/usr/bin/env python
#
# Lara Maia <dev@lara.click> 2015
#
# The Steam Tools is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# The Steam Tools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
#

import os
from logging import getLogger
from configparser import RawConfigParser

logger = getLogger('root')
config = RawConfigParser()
config.optionxform=str

def get_config_path(fileName):
    if os.name == 'nt':
        xdg_dir = os.getenv('LOCALAPPDATA')
    else:
        xdg_dir = os.getenv('XDG_CONFIG_HOME', os.path.join(os.path.expanduser('~'), '.config'))

    config_file = os.path.join(xdg_dir, 'steam-tools', fileName)
    os.makedirs(os.path.dirname(config_file), exist_ok=True)

    if os.path.isfile(fileName):
        return fileName
    else:
        if not os.path.isfile(config_file):
            logger.warn("No config file found.")
            logger.warn("Creating a new at %s", config_file)
            config.add_section('Config')
            with open(config_file, 'w') as fp:
                config.write(fp)
            
        return config_file

def read_config(fileName):
    config.read(get_config_path(fileName))
    return config

def write_config(fileName):
    with open(get_config_path(fileName), 'w') as fp:
        config.write(fp)
