import unittest

try:
    from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating
except ModuleNotFoundError:
    import sys, pathlib
    sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
    from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating


class TestGetOptionsRatio(unittest.TestCase):
    def test_normal(self):
        self.assertAlmostEqual(get_options_ratio(3, 10), 0.3)

    def test_zero_option(self):
        self.assertEqual(get_options_ratio(0, 5), 0.0)

    def test_equal_nums(self):
        self.assertEqual(get_options_ratio(5, 5), 1.0)

    def test_clamp_above_one(self):
        self.assertEqual(get_options_ratio(15, 10), 1.0)

    def test_total_must_be_positive(self):
        with self.assertRaises(ValueError):
            get_options_ratio(1, 0)
        with self.assertRaises(ValueError):
            get_options_ratio(1, -2)

    def test_option_must_be_nonnegative(self):
        with self.assertRaises(ValueError):
            get_options_ratio(-1, 5)


class TestGetFacultyRating(unittest.TestCase):
    def test_unacceptable_range(self):
        for r in [0.0, 0.10, 0.59, 0.60]:
            with self.subTest(r=r):
                self.assertEqual(get_faculty_rating(r), "Unacceptable")

    def test_needs_improvement_range(self):
        for r in [0.6000001, 0.61, 0.65, 0.70]:
            with self.subTest(r=r):
                self.assertEqual(get_faculty_rating(r), "Needs Improvement")

    def test_good_range(self):
        for r in [0.7000001, 0.71, 0.75, 0.80]:
            with self.subTest(r=r):
                self.assertEqual(get_faculty_rating(r), "Good")

    def test_very_good_range(self):
        for r in [0.8000001, 0.85, 0.8999999]:
            with self.subTest(r=r):
                self.assertEqual(get_faculty_rating(r), "Very Good")

    def test_excellent_range_and_edges(self):
        for r in [0.90, 0.95, 0.999999, 1.0, 1.2]:
            with self.subTest(r=r):
                self.assertEqual(get_faculty_rating(r), "Excellent")

    def test_negative_clamps_to_unacceptable(self):
        self.assertEqual(get_faculty_rating(-0.5), "Unacceptable")


if __name__ == "__main__":
    unittest.main()

