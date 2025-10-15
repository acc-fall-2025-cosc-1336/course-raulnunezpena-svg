from src.homework.e_functions.value_return import (
    get_gross_pay, get_fica_tax, get_federal_tax)

FICA_RATE = 0.0765   # 7.65%
FED_TAX_RATE = 0.08  # 8.00%


def test_gross_pay_no_overtime():
    result = get_gross_pay(40, 20)
    assert result == 800.00


def test_gross_pay_with_overtime():
    result = get_gross_pay(45, 20)
    # 40 * 20 = 800, 5 hours overtime * 20 * 1.5 = 150 → total = 950
    assert result == 950.00


def test_fica_tax():
    result = get_fica_tax(1000)
    assert round(result, 2) == 76.50


def test_federal_tax():
    result = get_federal_tax(1000)
    assert round(result, 2) == 80.00


def test_full_payroll_calculation():
    hours_worked = 45
    hourly_rate = 20

    gross_pay = get_gross_pay(hours_worked, hourly_rate)
    fica_tax = get_fica_tax(gross_pay)
    federal_tax = get_federal_tax(gross_pay)
    net_pay = gross_pay - fica_tax - federal_tax

    assert gross_pay == 950.00
    assert round(fica_tax, 3) == 72.675
    assert federal_tax == 76.00
    assert round(net_pay, 3) == 801.325

