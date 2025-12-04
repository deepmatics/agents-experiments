"""
This module initializes and provides the agents used in the application.
"""

from components.calculator import Calculator
from components.calculator import Calculator
from models.model_predictor import ModelPredictor
from config.config import config

def get_model_predictor():
    """Initializes and returns the ModelPredictor."""
    model_name = config.get('model')
    return ModelPredictor(model_name=model_name)

def get_calculator():
    """Initializes and returns the Calculator."""
    return Calculator()
