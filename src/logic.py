def add(num1, num2):
    return round(num1 + num2, 10)

def sub(num1, num2):
    return round(num1 - num2, 10)

def mul(num1, num2):
    return round(num1 * num2, 10)

def div(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Division error - dividing by zero")
    else:
        return round(num1 / num2, 10)

def factorial(num1):
    if num1 == 0:
        return 1
    elif num1 < 0:
        raise ValueError("Factorial error - number is smaller than 0")
    else:
        return round ((num1 * factorial(num1-1)), 10)

def exponentiation(num1, num2):
    if num2 < 0:
        raise ValueError("Exponentiation error - exponent is not a natural number")
    else:
        return round(num1 ** num2, 10)

def sqrt(num1, num2=2):
    if num1 < 0:
        raise ValueError("Root error - even degree of a negative radicant")
    else:
        return round((num1 ** (1./num2)), 10)

def abs(num1):
    if num1 >= 0:
        return round(num1, 10)
    else:
        return round((-num1), 10)