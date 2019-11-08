from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Square import squaree
from Calculator.Square_rot import squar_rot
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean


def psd(numbers):
    num_values = len(numbers)
    result3 = []
    result = mean(numbers)
    for numb in numbers:
        result2 = subtraction(numb, result)
        result3.append = squaree(result2)
        total=addition(total,result3.append)
    return squar_rot(division(num_values,total))

