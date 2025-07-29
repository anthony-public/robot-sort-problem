import unittest
from sort import sort

class TestSort(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(sort(10, 10, 10, 5), 'STANDARD')

    def test_bulky_by_volume(self):
        self.assertEqual(sort(100, 100, 100, 5), 'SPECIAL')  # volume = 1,000,000

    def test_bulky_by_dimension(self):
        self.assertEqual(sort(200, 10, 10, 5), 'SPECIAL')  # width >= 150

    def test_heavy(self):
        self.assertEqual(sort(10, 10, 10, 25), 'SPECIAL')  # mass >= 20

    def test_heavy_and_bulky(self):
        self.assertEqual(sort(200, 10, 10, 25), 'REJECTED')  # both conditions true

    def test_edge_case_volume(self):
        self.assertEqual(sort(100, 100, 100, 19.99), 'SPECIAL')  # volume exactly 1,000,000

    def test_edge_case_mass(self):
        self.assertEqual(sort(10, 10, 10, 20), 'SPECIAL')  # mass exactly 20

    def test_edge_case_dimension(self):
        self.assertEqual(sort(150, 10, 10, 5), 'SPECIAL')  # dimension exactly 150

    def test_standard_close_to_limits(self):
        self.assertEqual(sort(149, 10, 10, 19.9), 'STANDARD')  # just under limits

if __name__ == "__main__":
    unittest.main()
