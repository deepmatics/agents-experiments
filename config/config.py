"""
This module loads the configuration from a YAML file and makes it available to the application.
"""

import yaml

def load_config(config_path='config/config.yaml'):
    """Loads the configuration from a YAML file."""
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

config = load_config()