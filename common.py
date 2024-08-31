
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
