import unittest

from Statistics.Statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_median(self):
        self.assertEqual(self.statistics.median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)

    def test_mode(self):
        self.assertEqual(self.statistics.mod([2, 9, 9, 7, 9, 2, 4, 5, 8]), 9)

    def test_psd(self):
        self.assertEqual(self.statistics.psd([1,2,4,5,8]),2.4495)
if __name__ == '__main__':
    unittest.main()
