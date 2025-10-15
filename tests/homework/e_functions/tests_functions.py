import unittest

from src.homework.e_functions.value_return import get_gross_pay, get_fica_tax, get_federal_tax

FICA_RATE = 0.0765   # 7.65%
FED_TAX_RATE = 0.08  # 8.00%

def test_get_gross_pay(self):
    result = get_gross_pay(40, 10)
    self.assertEqual(result, 400)

def test_get_gross_pay_overtime(self):
    result = get_gross_pay(45, 10)
    self.assertEqual(result, 475)  # 40*10 + 5*15

def test_get_fica_tax(self):
    result = get_fica_tax(1000)
    self.assertAlmostEqual(result, 76.5)

def get_federal_tax(self):
    result = get_federal_tax(1000)
    self.assertAlmostEqual(result, 80.0)

def get_full_pay_calculation(self):
    hours_worked = 45
    hourly_rate = 10
    gross_pay = get_gross_pay(hours_worked, hourly_rate)
    fica_tax = get_fica_tax(gross_pay)
    federal_tax = get_federal_tax(gross_pay)
    net_pay = gross_pay - fica_tax - federal_tax
    self.assertEqual(gross_pay, 475)
    self.assertAlmostEqual(fica_tax, 36.3375)
    self.assertAlmostEqual(federal_tax, 38.0)
    self.assertAlmostEqual(net_pay, 400.6625)
     #end of file















  

