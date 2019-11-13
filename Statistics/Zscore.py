from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean
from Statistics.Psd import psd


def zscore(numbers):
    standartdev = (psd(numbers))
    m = mean(numbers)
    for numb in numbers:
        result = subtraction(numb, m)
        return division(standartdev, result)
