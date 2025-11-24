import unittest
from tests.homework.g_lists_and_tuples import tests_lists_and_tuples as tests_strings

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(tests_strings)
    unittest.TextTestRunner().run(suite)
    
