"""
This module contains the Flask application.
"""

from flask import Flask, request, jsonify
from utils.logger import get_logger
from components.calculator import Calculator
from models.model_predictor import ModelPredictor
import re

app = Flask(__name__)
logger = get_logger(__name__)

calculator = Calculator()
model_predictor = ModelPredictor(model_name="gemini-pro") # Assuming a default model name here

math_pattern = re.compile(r'^\s*([-+]?\d*\.?\d+([eE][-+]?\d+)?)\s*([-+*/])\s*([-+]?\d*\.?\d+([eE][-+]?\d+)?)\s*$')


@app.route('/predict', methods=['POST'])
def predict():
    """Predicts the output for a given input by calling the appropriate tool.
    """
    data = request.json
    input_text = data.get('input', '')
    logger.info(f"Received input: {input_text}")
    
    if math_pattern.match(input_text):
        result = calculator.calculate(input_text)
    else:
        result = model_predictor.predict(input_text)
    
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)