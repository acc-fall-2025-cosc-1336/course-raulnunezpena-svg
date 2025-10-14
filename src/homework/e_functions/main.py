from value_return import get_gross_pay, get_fica_tax, get_federal_tax
from void_func import print_pay_details

def main():
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))

    gross_pay = get_gross_pay(hours_worked, hourly_rate)
    fica_tax = get_fica_tax(gross_pay)
    federal_tax = get_federal_tax(gross_pay)

    print_pay_details(gross_pay, fica_tax, federal_tax)

if __name__ == "__main__":
    main()
 
