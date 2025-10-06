# tests/homework/d_repetition/tests_repetition.py
import unittest

from src.homework.d_repetition.repetition import(
    get_factorial,
    sum_odd_numbers,)


class Test_Config(unittest.TestCase):
    # ------- get_factorial -------
    def test_factorial_0(self):
        self.assertEqual(get_factorial(0), 1)

    def test_factorial_1(self):
        self.assertEqual(get_factorial(1), 1)

    def test_factorial_5(self):
        self.assertEqual(get_factorial(5), 120)

    def test_factorial_9(self):
        self.assertEqual(get_factorial(9), 362880)

    def test_factorial_negative_raises(self):
        with self.assertRaises(ValueError):
            get_factorial(-3)

    def test_factorial_nonint_raises(self):
        with self.assertRaises(ValueError):
            get_factorial(3.2)

    # ------- sum_odd_numbers -------
    def test_sum_odds_1(self):
        self.assertEqual(sum_odd_numbers(1), 1)          # 1

    def test_sum_odds_6(self):
        self.assertEqual(sum_odd_numbers(6), 9)          # 1+3+5

    def test_sum_odds_7(self):
        self.assertEqual(sum_odd_numbers(7), 16)         # 1+3+5+7

    def test_sum_odds_99(self):
        # formula check: sum of first k odd numbers = k^2; for n=99 (odd), k=(99+1)//2=50 -> 2500
        self.assertEqual(sum_odd_numbers(99), 2500)

    def test_sum_odds_even_ceiling(self):
        # even n should sum only up to n-1
        self.assertEqual(sum_odd_numbers(10), 25)        # 1+3+5+7+9

    def test_sum_odds_zero_raises(self):
        with self.assertRaises(ValueError):
            sum_odd_numbers(0)

    def test_sum_odds_nonint_raises(self):
        with self.assertRaises(ValueError):
            sum_odd_numbers(8.5)

if __name__ == "__main__":
    unittest.main(verbosity=2)
    

