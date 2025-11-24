import unittest
from src.homework.c_decisions.decisions import get_letter_grade
class TestDecisions(unittest.TestCase):
    def test_A_grade(self):
        self.assertEqual(get_letter_grade(95), "A")

    def test_B_grade(self):
        self.assertEqual(get_letter_grade(85), "B")

    def test_C_grade(self):
        self.assertEqual(get_letter_grade(75), "C")

    def test_D_grade(self):
        self.assertEqual(get_letter_grade(65), "D")

    def test_F_grade(self):
        self.assertEqual(get_letter_grade(50), "F")

    def test_invalid_high(self):
        self.assertEqual(get_letter_grade(105), "Invalid grade")

    def test_invalid_low(self):
        self.assertEqual(get_letter_grade(-5), "Invalid grade")
