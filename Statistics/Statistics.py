from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.SampleMean import sample_mean
from Statistics.Median import median
from Statistics.Mode import mod
from Statistics.Psd import psd
from CsvReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result

    def sample_mean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result

    def median(self):
        self.result = median(self.data)
        return self.result

    def mod(self):
        self.result = mod(self.data)
        return self.result

    def psd(self):
        self.result = psd(self.data)
