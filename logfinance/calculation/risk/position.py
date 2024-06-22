# logfinance/logfinance.py

import math

class PositionRisk:
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def log_finance(number, base=math.e):
        """Calculate the logarithm of a number with an optional base."""
        if number <= 0:
            raise ValueError("Number must be greater than 0")
        return math.log(number, base)
    
    def hello(self):
        return "Hello, World!"