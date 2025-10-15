# /src/homework/e_functions/main.py

from value_return import get_gross_pay, get_fica_tax, get_federal_tax
from void_func import display_payroll_check

def main():
    # Input
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))

    # Calculations
    gross_pay = get_gross_pay(hours_worked, hourly_rate)
    fica_tax = get_fica_tax(gross_pay)
    federal_tax = get_federal_tax(gross_pay)
    net_pay = gross_pay - fica_tax - federal_tax

    # Display (void)
    display_payroll_check(gross_pay, fica_tax, federal_tax, net_pay)

if __name__ == "__main__":
    main()
