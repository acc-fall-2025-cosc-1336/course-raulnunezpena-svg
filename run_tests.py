import unittest
from tests.homework.h_strings import tests_strings

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(tests_strings)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
