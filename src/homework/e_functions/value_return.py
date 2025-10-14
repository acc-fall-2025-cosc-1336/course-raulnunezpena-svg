FICA_RATE = 0.0765   # 7.65%
FED_TAX_RATE = 0.08  # 8.00%

def get_gross_pay(hours, rate):
    """Compute gross pay with overtime (time-and-a-half over 40 hours)."""
    if hours < 0 or rate < 0:
        raise ValueError("hours and rate must be non-negative")
    regular_hours = hours if hours <= 40 else 40
    overtime_hours = hours - 40 if hours > 40 else 0
    gross = regular_hours * rate + overtime_hours * rate * 1.5
    return gross

def get_fica_tax(gross_pay):
    """Compute FICA tax using global FICA_RATE on gross pay."""
    if gross_pay < 0:
        raise ValueError("gross_pay must be non-negative")
    return gross_pay * FICA_RATE

def get_federal_tax(gross_pay):
    """Compute Federal tax using global FED_TAX_RATE on gross pay."""
    if gross_pay < 0:
        raise ValueError("gross_pay must be non-negative")
    return gross_pay * FED_TAX_RATE