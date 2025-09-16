# Named constant for sales tax rate
TAX_RATE = 0.0675

def get_sales_tax_amount(meal_amount: float) -> float:
    """
    Calculate sales tax based on the meal amount.
    """
    return meal_amount * TAX_RATE

def get_tip_amount(meal_amount: float, tip_rate: float) -> float:
    """
    Calculate tip amount based on the meal amount and tip rate.
    tip_rate should be given as a decimal (e.g., 0.15 for 15%).
    """
    return meal_amount * tip_rate
