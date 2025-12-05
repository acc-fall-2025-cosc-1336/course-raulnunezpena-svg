

import unittest
from src.homework.g_lists_and_tuples.lists import get_p_distance, get_p_distance_matrix


class TestListsAndTuples(unittest.TestCase):

    def test_get_p_distance(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']

        # from the assignment: these should have p-distance 0.4
        expected = 0.4
        self.assertAlmostEqual(get_p_distance(list1, list2), expected)

    def test_get_p_distance_matrix(self):
        dna_lists = [
            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A']
        ]

        expected_matrix = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]

        result = get_p_distance_matrix(dna_lists)

        # compare each cell with a small tolerance
        for i in range(len(expected_matrix)):
            for j in range(len(expected_matrix[i])):
                self.assertAlmostEqual(result[i][j], expected_matrix[i][j], places=5)


if __name__ == "__main__":
    unittest.main()
