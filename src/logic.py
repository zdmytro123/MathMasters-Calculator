#!/usr/bin/env python3
###################################################################
# Project name: MathMasters-Calculator
# File: logic.py
# Authors: Daria Kinash
# Description: Math Library with basic mathematical operations
###################################################################


##
# @file logic.py
# @author Vilem Gottwald, Pavel Marek
# @brief  Math Library with basic mathematical operations
#


##
# @brief Function of adding two numbers
#
# @param num1 First number
# @param num2 Second number
#
# @return  Returns sum of two numbers
def add(num1, num2):
    return round(num1 + num2, 10)


##
# @brief Function of subtracting one number from another
#
# @param num1 First number
# @param num2 Second number
#
# @return  Returns difference between two numbers
def sub(num1, num2):
    return round(num1 - num2, 10)


##
# @brief Function of multiplying two numbers
#
# @param num1 First number
# @param num2 Second number
#
# @return  Returns product of two numbers
def mul(num1, num2):
    return round(num1 * num2, 10)


##
# @brief Function to divide two numbers
#
# @param num1 First number
# @param num2 Second number
#
# @return  Returns quotient of two numbers
def div(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Division error - dividing by zero")
    else:
        return round(num1 / num2, 10)


##
# @brief Function to calculate factorial.
#
# @param num Number
#
# @return Returns factorial of given number
def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        raise ValueError("Factorial error - number is smaller than 0")
    else:
        return round ((num * factorial(num-1)), 10)


##
# @brief Function to calculate power
#
# @param num1 Base
# @param num2 Exponent
#
# @return Returns result of the exponentiation
def exponentiation(num1, num2):
    if num2 < 0:
        raise ValueError("Exponentiation error - exponent is not a natural number")
    else:
        return round(num1 ** num2, 10)


##
# @brief Function to calculate root
#
# @param num1 Radicand
# @param num2 Index
#
# @return Returns result of the root
def sqrt(num1, num2=2):
    if num1 < 0:
        raise ValueError("Root error - even degree of a negative radicant")
    else:
        return round((num1 ** (1./num2)), 10)


##
# @brief Function to calculate the absolute value of a given number
#
# @param num Number
#
# @return Returns absolute value of a given number
def abs(num):
    if num >= 0:
        return round(num, 10)
    else:
        return round((-num), 10)
    
# End of file logic.py