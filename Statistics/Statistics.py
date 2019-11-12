from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.SampleMean import sample_mean
from Statistics.Median import median
from Statistics.Mode import mod
from Statistics.Psd import psd
from Statistics.Vpp import vpp
from Statistics.Zscore import zscore
from CsvReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self):
        d = []
        for row in self.data.data:
            d.append(row['v'])
        self.result = mean(d)
        return self.result

    def sample_mean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result

    def median(self):
        d = []
        for row in self.data.data:
            d.append(row['v'])
        self.result = median(d)
        return self.result

    def mod(self):
        d = []
        for row in self.data.data:
            d.append(row['v'])
        self.result = mod(d)
        return self.result

    def psd(self):
        d = []
        for row in self.data.data:
            d.append(row['v'])
        self.result = psd(d)
        return self.result

    def vpp(self):
        d = []
        for row in self.data.data:
            d.append(row['v'])
        self.result = vpp(d)
        return self.result

    def z_score(self, a):
        self.result = zscore(a)
        return self.result