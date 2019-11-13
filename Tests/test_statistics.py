import unittest

from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
       # self.statistics = Statistics()
      self.statistics = Statistics("/Tests/Data/Stat.csv")

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        self.assertEqual(self.statistics.mean(), 4.0)

    def test_median(self):
        #test_data = CsvReader("Tests/Data/mean.csv").data
        #result = float(row['r'])
        self.assertEqual(self.statistics.median(),4)

    def test_mode(self):
        self.assertEqual(self.statistics.mod(), 1)

    def test_psd(self):
        self.assertEqual(round(self.statistics.psd(), 4), 2.4495)

    def test_vpp(self):

        self.assertEqual(self.statistics.vpp(), 6)

    # def test_zscore(self):
    #     #self.statistics = Statistics("Tests/Data/zscore.csv")
    #     test_data = CsvReader("Tests/Data/zscore.csv").data
    #     for row in test_data:
    #         result = float(row['Result'])
    #         self.assertEqual(self.statistics.zscore(row['v']), result)


if __name__ == '__main__':
    unittest.main()
