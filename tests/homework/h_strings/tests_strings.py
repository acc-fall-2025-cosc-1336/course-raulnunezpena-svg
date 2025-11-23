import unittest
from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement


class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        dna1 = "AAAA"
        dna2 = "AAAT"
        self.assertEqual(get_hamming_distance(dna1, dna2), 1)

    def test_get_dna_complement(self):
        dna = "AAGT"
        self.assertEqual(get_dna_complement(dna), "ACTT")


if __name__ == "__main__":
    unittest.main()
