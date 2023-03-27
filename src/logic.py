def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("Error: division by zero")
        return None
    else:
        return num1 / num2

def factorial(num1):
    if num1 == 0:
        return 1
    elif num1 < 0:
        print("Error: factorial of negative number")
        return None
    else:
        return num1 * factorial(num1-1)

def exponentiation(num1, num2):
    if num2 < 0:
        print("Error: exponent is negative")
        return None
    else:
        return num1 ** num2

def sqrt(num1, num2=2):
    if num1 < 0:
        print("Error: square root of negative number")
        return None
    else:
        return num1 ** (1./num2)
