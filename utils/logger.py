"""
This module provides a simple logger configuration.
"""

import logging

def get_logger(name):
    """Returns a configured logger."""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(name)
    return logger