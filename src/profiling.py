#!/usr/bin/env python3

##
# @file     profiling.py
# @brief    Program to calculate the sample standard deviation
# @author   Daria Kinash
#Run the tests in the src directory by
#typing the command: $ python3 profiling.py < data.txt, where data.txt - file containing numbers with whitespace without separator

from logic import *
import sys

##
# @brief Function to calculate the sample standard deviation
#
# @param numbers List of numbers to calculate standard deviation
#
# @return Returns standard deviation
def sample_std_deviation(numbers):
    n = len(numbers)
    mean = div(sum(numbers),n)
    variance = div((sum([exponentiation( (sub(x, mean)), 2) for x in numbers])), (n-1))
    return sqrt(variance)

##
# @brief Read redirected input from standard input
numbers = []
for line in sys.stdin:
    numbers.extend(map(float, line.split()))

std_deviation = sample_std_deviation(numbers)
print(std_deviation)



