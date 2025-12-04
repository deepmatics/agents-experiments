"""
This module contains the Calculator agent.
"""

from asteval import Interpreter

class Calculator:
    """A calculator agent that safely evaluates mathematical expressions."""
    def __init__(self):
        self.aeval = Interpreter()

    def calculate(self, expression):
        """Calculates the result of a mathematical expression.

        Args:
            expression: The mathematical expression to evaluate.

        Returns:
            The result of the calculation or an error message.
        """
        try:
            return self.aeval.eval(expression)
        except Exception as e:
            return f"Error: {e}"