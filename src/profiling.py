from logic import *
import sys 

def sample_std_deviation(numbers):
    n = len(numbers)
    mean = div(sum(numbers),n)
    variance = div((sum([exponentiation( (sub(x, mean)), 2) for x in numbers])), (n-1))
    return sqrt(variance)

numbers = []
for line in sys.stdin:
    numbers.extend(map(float, line.split()))

std_deviation =sample_std_deviation(numbers)
print(std_deviation)




