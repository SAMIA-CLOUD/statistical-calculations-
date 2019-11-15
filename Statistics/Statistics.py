from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.SampleMean import sample_mean
from Statistics.Median import median
from Statistics.Mode import mod
from Statistics.Psd import psd
from Statistics.Vpp import vpp
from Statistics.Zscore import zscore
from CsvReader.CsvReader import CsvReader
from CsvReader.FetchRawData import fetchRawdata


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self):
        self.result = mean(fetchRawdata(self.data, 'v'))
        return self.result

    def sample_mean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result

    def median(self):
        self.result = median(fetchRawdata(self.data, 'v'))
        return self.result

    def mod(self):
        self.result = mod(fetchRawdata(self.data, 'v'))
        return self.result

    def psd(self):
        self.result = psd(fetchRawdata(self.data, 'v'))
        return self.result

    def vpp(self):
        self.result = vpp(fetchRawdata(self.data, 'v'))
        return self.result

    def z_score(self, a):
        self.result = zscore(a)
        return self.result
