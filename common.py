#
# Copyright (C) 2024 Simon Howard
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version. This program is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#

from os.path import dirname, join, exists
import yaml

def read_config(path):
    if path == '':
        return {}

    # Config deeper in the hierarchy can override config files from
    # higher up in the hierarchy:
    result = read_config(dirname(path))
    config_file = join(path, ".democonfig")
    if exists(config_file):
        with open(config_file) as f:
            result.update(yaml.safe_load(f))

    return result
