"""
This module contains the ModelPredictor agent.
"""

from transformers import pipeline
from utils.logger import get_logger

logger = get_logger(__name__)

class ModelPredictor:
    """A text prediction agent that uses a pre-trained model."""
    def __init__(self, model_name):
        """Initializes the ModelPredictor with the given model name."""
        self.model = pipeline('text-generation', model=model_name)
    
    def predict(self, input_text):
        """Predicts the output for a given input text.

        Args:
            input_text: The input text for prediction.

        Returns:
            The predicted text.
        """
        logger.info(f"Predicting for input: {input_text}")
        return self.model(input_text, max_length=50)[0]['generated_text']