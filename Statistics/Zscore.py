from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean
from Statistics.Psd import psd


def zscore(numbers):
    row_value = 484
    sd = psd(numbers)
    m = mean(numbers)
    result = subtraction(row_value, m)
    return division(sd, result)
