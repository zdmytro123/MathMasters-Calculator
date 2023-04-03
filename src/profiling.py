from logic import *
import sys 

def sample_std_deviation(numbers):
    n = len(numbers)
    mean = div(sum(numbers),n)
    variance = div(sum(sub((exponentiation(x, 2) for x in numbers), multiply(n, (exponentiation(mean, 2))))), (n-1))
    return sqrt(variance)

numbers = []
for line in sys.stdin:
    numbers.extend(map(float, line.split()))

std_deviation =sample_std_deviation(numbers)
print(std_deviation)




