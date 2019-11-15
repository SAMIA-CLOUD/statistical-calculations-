import statistics
from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Square import squaree
from Calculator.Square_rot import squar_rot
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean
from Statistics.Getsample import getSample
import random


def ssd(data):
    total = 0
    sample = random.randint(1, len(data))
    new_sample = getSample(data, sample)
    n = len(new_sample)
    new_mean = mean(new_sample)
    for numb in new_sample:
        result = subtraction(numb, new_mean)
        sq = squaree(result)
        total = addition(total, sq)
    d = division(subtraction(n, 1), total)
    samp_sd = squar_rot(d)
    actual_sd = statistics.stdev(new_sample)
    return samp_sd, actual_sd

# def ssd(data,sample_size):
#     total=0
#     sample = getSample(data, sample_size)
#     n = len(sample)
#     new_mean=mean(sample)
#     for numb in sample:
#         result = subtraction(numb, new_mean)
#         sq = squaree(result)
#         total = addition(total, sq)
#     d=division(subtraction(n, 1), total)
#     samp_sd = squar_rot(d)
#     return samp_sd
