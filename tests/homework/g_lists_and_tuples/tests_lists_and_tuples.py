import unittest
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value
from src.homework.g_lists_and_tuples.lists import get_highest_list_value

class Test_Config(unittest.TestCase):

    def test_get_lowest_list_value(self):
        values = [3, 1, 4, 1, 5]
        self.assertEqual(get_lowest_list_value(values), 1)

    
    def test_get_highest_list_value(self):
        values = [3, 1, 4, 1, 5]
        self.assertEqual(get_highest_list_value(values), 5)


if __name__ == "__main__":
    unittest.main()
