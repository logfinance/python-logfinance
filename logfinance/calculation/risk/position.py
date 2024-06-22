# logfinance/logfinance.py

import math

class PositionRisk:
    
    def __init__(self) -> None:
        pass
        
    @staticmethod
    def calculate_position_details(current_price, risk_reward_ratio, usd_amount):
        """Calculate the position size, take profit, and stop loss based on the current price, risk-reward ratio, and USD amount."""
        if current_price <= 0 or risk_reward_ratio <= 0 or usd_amount <= 0:
            raise ValueError("Inputs must be greater than 0")
        
        position_size = usd_amount / current_price
        take_profit = current_price * risk_reward_ratio
        stop_loss = current_price / risk_reward_ratio
        
        return {
            "position_size": position_size,
            "take_profit": take_profit,
            "stop_loss": stop_loss
        }

    @staticmethod
    def calculate_liquidation_price(leverage, fee_percentage, entry_price, sl): 
        """Calculate the liquidation price based on the leverage, fee, entry price, stop loss, and take profit."""
        fee = fee_percentage / 100  # Convert fee from percentage to decimal
        
        if leverage <= 0 or fee <= 0 or entry_price <= 0 or sl <= 0:
            raise ValueError("Inputs must be greater than 0")
        
        liquidation_price = entry_price - (entry_price - sl) / leverage - (fee * entry_price) / leverage
        
        return liquidation_price

    @staticmethod
    def calculate_stop_loss(liquidation_price, leverage, entry_price, fee_percentage):
        """Calculate the stop loss based on the liquidation price, leverage, entry price, and fee percentage."""
        fee = fee_percentage / 100  # Convert fee from percentage to decimal
        
        if leverage <= 0 or fee <= 0 or entry_price <= 0 or liquidation_price <= 0:
            raise ValueError("Inputs must be greater than 0")
        
        stop_loss = entry_price - (entry_price - liquidation_price) * leverage - (fee * entry_price) * leverage
        
        return stop_loss
    
    