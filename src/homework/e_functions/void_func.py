def display_payroll_check(gross_pay, fica_tax, federal_tax, net_pay):
    """
    Void function: prints the payroll check details with fixed-width money formatting.
    The assignment’s sample formatting is matched (aligned, 2 decimals).
    """
    print(f"  Gross Pay:       {gross_pay:10.2f}")
    print(f"  FICA:            {fica_tax:10.2f}")
    print(f"  Federal Tax:     {federal_tax:10.2f}")
    print(f"  Net Pay:         {net_pay:10.2f}")