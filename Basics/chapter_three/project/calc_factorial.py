"""
calculating the factorial
"""
import math


def calf_factorial(num):
    result = 0
    for x in num:
        result += math.factorial(x)
    return result
