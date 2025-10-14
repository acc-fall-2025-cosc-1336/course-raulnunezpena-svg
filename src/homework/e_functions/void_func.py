from value_return import get_gross_pay, get_fica_tax, get_federal_tax

def print_pay_details(hours_worked, hourly_rate):
    gross_pay = get_gross_pay(hours_worked, hourly_rate)
    fica_tax = get_fica_tax(gross_pay)
    federal_tax = get_federal_tax(gross_pay)
    net_pay = gross_pay - fica_tax - federal_tax

    print(f"Hours Worked: {hours_worked}")
    print(f"Hourly Rate: ${hourly_rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"FICA Tax: ${fica_tax:.2f}")
    print(f"Federal Tax: ${federal_tax:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")


    