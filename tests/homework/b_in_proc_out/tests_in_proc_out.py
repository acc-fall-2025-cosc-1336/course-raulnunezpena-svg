import unittest
from src.homework.b_in_proc_out.in_proc_out import (
    get_sales_tax_amount, get_tip_amount, calculate_total
)

class TestRestaurantBill(unittest.TestCase):
    def test_get_sales_tax_amount(self):
        self.assertAlmostEqual(get_sales_tax_amount(100), 6.75, places=2)

    def test_get_tip_amount(self):
        self.assertAlmostEqual(get_tip_amount(100, 20), 20.0, places=2)

    def test_calculate_total(self):
        receipt = calculate_total(100, 20)
        self.assertAlmostEqual(receipt["meal"], 100.0, places=2)
        self.assertAlmostEqual(receipt["tax"], 6.75, places=2)
        self.assertAlmostEqual(receipt["tip"], 20.0, places=2)
        self.assertAlmostEqual(receipt["total"], 126.75, places=2)

if __name__ == "__main__":
    unittest.main()

