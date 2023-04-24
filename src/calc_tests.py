#!/usr/bin/env python3
###################################################################
# Project name: MathMasters-Calculator
# File: calc_tests.py
# Authors: Azatbek Tergeussov
# Description: Test for mathematical library
###################################################################

##
# @file calc_tests.py
# @author Azatbek Tergeussov
# @brief Test for mathematical library
#

# Run the tests in the src directory by typing the command:
# $ python3 calc_tests.py
# or 
# $ python3 -m unittest calc_tests.py

import unittest
import math
from logic import *



# @brief Tests of function add()
class TestsCalculator_addition(unittest.TestCase):

    def setUp(self):
        self.number_1 = 1
        self.number_2 = 2
        self.number_3 = 3     
        self.Decimal_1 = 1.4573534
        self.Decimal_2 = 2.3465463
        self.Negnumber_1 = -234
        self.Negnumber_2 = -85
        self.a = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        self.b = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    
    def test_Add_InputExists(self):        
        self.assertIsNotNone(self.number_1)
        self.assertIsNotNone(self.number_2)
        self.assertIsNotNone(self.number_3)
        self.assertIsNotNone(self.Decimal_1)
        self.assertIsNotNone(self.Decimal_2)
        self.assertIsNotNone(self.Negnumber_1)
        self.assertIsNotNone(self.Negnumber_2)
        self.assertIsNotNone(self.a)
        self.assertIsNotNone(self.b)
    
    def test_Add_NumberType(self):             
        self.assertIsInstance(self.number_1, (int, float))
        self.assertIsInstance(self.number_2, (int, float))
        self.assertIsInstance(self.number_3, (int, float))
        self.assertIsInstance(self.Decimal_1, (int, float))
        self.assertIsInstance(self.Decimal_2, (int, float))
        self.assertIsInstance(self.Negnumber_1, (int, float))
        self.assertIsInstance(self.Negnumber_2, (int, float))
        self.assertIsInstance(self.a, (int, float))
        self.assertIsInstance(self.b, (int, float))
    
    def test_Returns_Addition(self):        
        result = add(self.number_1, self.number_2)
        expected_result = self.number_1 + self.number_2
        self.assertEqual(result, expected_result)

    def test_Add_Commutativity(self):       
        result1 = add(self.number_1, self.number_2)
        result2 = add(self.number_2, self.number_1)
        self.assertEqual(result1, result2)
    
    def test_Add_Associativity(self):          
        result1 = add(self.number_1, add(self.number_2, self.number_3))
        result2 = add(add(self.number_1, self.number_2), self.number_3)
        self.assertEqual(result1, result2)
       
    def test_Add_Identity(self):                
        result = add(self.number_1, 0)
        self.assertEqual(result, self.number_1)
    
    def test_Add_LargeNumbers(self):
        result1 = add(self.a, self.b)
        result2 = self.a + self.b
        self.assertEqual(result1, result2)
    
    def test_Add_DecimalNumbers(self):        
        result1 = add(self.Decimal_1, self.Decimal_2)
        result2 = self.Decimal_1 + self.Decimal_2
        self.assertAlmostEqual(result1, result2, places=2) 
    
    def test_Add_NegativeNumbers(self):            
        result = add(self.Negnumber_1, self.Negnumber_2)
        expected_result = self.Negnumber_1 + self.Negnumber_2
        self.assertEqual(result, expected_result)
    
    def test_Add_Negative_To_Positive(self):     
        result = add(self.Negnumber_1, self.number_3)
        expected_result = self.Negnumber_1 + self.number_3
        self.assertEqual(result, expected_result)
    

    
# @brief Tests of function sub() 
class TestsCalculator_substraction(unittest.TestCase):

    def setUp(self):
        self.number_1 = 5
        self.number_2 = 1
        self.Negnumber_3 = -23
        self.Decimal_1 = 6.789
        self.Decimal_2 = 1.5
        self.a = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        self.b = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    
    def test_Sub_InputExists(self):                
        self.assertIsNotNone(self.number_1)
        self.assertIsNotNone(self.number_2)
        self.assertIsNotNone(self.Negnumber_3)
        self.assertIsNotNone(self.Decimal_1)
        self.assertIsNotNone(self.Decimal_2)
        self.assertIsNotNone(self.a)
        self.assertIsNotNone(self.b)
    
    def test_Sub_NumberType(self):                 
        self.assertIsInstance(self.number_1, (int, float))
        self.assertIsInstance(self.number_2, (int, float))
        self.assertIsInstance(self.Negnumber_3, (int, float))
        self.assertIsInstance(self.Decimal_1, (int, float))
        self.assertIsInstance(self.Decimal_2, (int, float))
        self.assertIsInstance(self.a, (int, float))
        self.assertIsInstance(self.b, (int, float))
    
    def test_Returns_Substraction(self):        
        result = sub(self.number_1, self.number_2)
        expected_result = self.number_1 - self.number_2
        self.assertEqual(result, expected_result)
    
    def test_Sub_NegativNumbers(self):           
        result = sub(self.Negnumber_3, self.Decimal_1)
        expected_result = self.Negnumber_3 - self.Decimal_1
        self.assertEqual(result, expected_result)
    
    def test_Sub_Negative_From_Positive(self):       
        result = sub(self.number_1, self.Negnumber_3)
        expected_result = self.number_1 - self.Negnumber_3
        self.assertEqual(result, expected_result)
    
    def test_Sub_Positive_From_Negative(self):    
        result = sub(self.Negnumber_3, self.number_1)
        expected_result = self.Negnumber_3 - self.number_1
        self.assertEqual(result, expected_result)
    
    def test_Sub_LargeNumbers(self):
        result1 = sub(self.a, self.b)
        result2 = self.a - self.b
        self.assertEqual(result1, result2)
    
    def test_Sub_DecimalNumbers(self):
        result = sub(self.Decimal_1, self.Decimal_2)
        expected_result = self.Decimal_1 - self.Decimal_2
        self.assertAlmostEqual(result, expected_result, places=2)
    
    def test_Sub_Identity(self):  
        result = sub(self.number_1, 0)
        self.assertEqual(result, self.number_1)



# @brief Tests of function mul()
class TestCalculator_multiplication(unittest.TestCase):

    def setUp(self):
        self.number_1 = 5 
        self.number_2 = 9
        self.Negnumber_1 = -5
        self.Negnumber_2 = -9
        self.Decimal_1 = 1.3
        self.Decimal_2 = 21.324
        self.a = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        self.b = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    
    def test_Mul_InputExists(self):
        self.assertIsNotNone(self.number_1)
        self.assertIsNotNone(self.number_2)
        self.assertIsNotNone(self.Negnumber_1)
        self.assertIsNotNone(self.Negnumber_2)
        self.assertIsNotNone(self.Decimal_1)
        self.assertIsNotNone(self.Decimal_2)
        self.assertIsNotNone(self.a)
        self.assertIsNotNone(self.b)
    
    def test_Mul_NumberType(self):
        self.assertIsInstance(self.number_1, (int, float))
        self.assertIsInstance(self.number_2, (int, float))
        self.assertIsInstance(self.Negnumber_1, (int, float))
        self.assertIsInstance(self.Negnumber_2, (int, float))
        self.assertIsInstance(self.Decimal_1, (int, float))
        self.assertIsInstance(self.Decimal_2, (int, float))
        self.assertIsInstance(self.a, (int, float))
        self.assertIsInstance(self.b, (int, float))

    def test_Returns_Multiplication(self):
        result = (mul(self.number_1, self.number_2))
        expected_result = self.number_1 * self.number_2
        self.assertEqual(result, expected_result)
    
    def test_Mul_Commutativity(self):          
        result1 = mul(self.number_1, self.number_2)
        result2 = mul(self.number_2, self.number_1)
        self.assertEqual(result1, result2)
    
    def test_Mul_Identity(self):               
        result = mul(self.number_1, 1)
        self.assertEqual(result, self.number_1)
    
    def test_Mul_Zero(self):
        result = mul(self.number_1, 0)
        self.assertEqual(result, 0)
    
    def test_Mul_NegativeNumbers(self):
        result = mul(self.Negnumber_1, self.Negnumber_2)
        expected_result = self.Negnumber_1 * self.Negnumber_2
        self.assertEqual(result, expected_result)
    
    def test_Mul_Negative_And_Positive(self):
        result = mul(self.Negnumber_1, self.number_2)
        expected_result = self.Negnumber_1 * self.number_2
        self.assertEqual(result, expected_result)
    
    def test_Mul_DecimalNumbers(self):
        result = mul(self.Decimal_1, self.Decimal_2)
        expected_result = self.Decimal_1 * self.Decimal_2
        self.assertAlmostEqual(result, expected_result, places=2)
    
    def test_Mul_Decimal_And_Zero(self):
        result = mul(self.Decimal_1, 0)
        self.assertEqual(result, 0)
    
    def test_Mul_LargeNumbers(self):
        result1 = mul(self.a, self.b)
        result2 = self.a * self.b
        self.assertEqual(result1, result2)
    
    

# @brief Tests of function div ()  
class TestCalculator_division(unittest.TestCase):

    def setUp(self):
        self.number_1 = 21
        self.number_2 = 7
        self.Negnumber_1 = -21
        self.Negnumber_2 = -7    
        self.Decimal_1 = 3.0
        self.Decimal_2 = 12.4325
        self.a = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        self.b = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        self.small = 0.00000000001
    
    def test_Div_InputExists(self):            
        self.assertIsNotNone(self.number_1)
        self.assertIsNotNone(self.number_2)
        self.assertIsNotNone(self.Negnumber_1)
        self.assertIsNotNone(self.Negnumber_2)
        self.assertIsNotNone(self.Decimal_1)
        self.assertIsNotNone(self.Decimal_2)
        self.assertIsNotNone(self.a)
        self.assertIsNotNone(self.b)
    
    def test_Div_NumberType(self):              
        self.assertIsInstance(self.number_1, (int, float))
        self.assertIsInstance(self.number_2, (int, float))
        self.assertIsInstance(self.Negnumber_1, (int, float))
        self.assertIsInstance(self.Negnumber_2, (int, float))
        self.assertIsInstance(self.Decimal_1, (int, float))
        self.assertIsInstance(self.Decimal_2, (int, float))
        self.assertIsInstance(self.a, (int, float))
        self.assertIsInstance(self.b, (int, float))
    
    def test_Returns_Division(self):        
        result = div(self.number_1, self.number_2)
        expected_result = self.number_1 / self.number_2
        self.assertEqual(result, expected_result)
    
    def test_Div_Integer(self):
        result = div(self.number_1, self.number_2)
        expected_result = self.number_1 / self.number_2
        self.assertEqual(result, expected_result)
    
    def test_FloatDivision(self):
        result = div(self.Decimal_1, self.Decimal_2)
        expected_result = self.Decimal_1 / self.Decimal_2
        self.assertAlmostEqual(result, expected_result, places=2)
   
    def test_Div_Negative_By_Positive(self):
        result = div(self.Negnumber_1, self.number_2)
        expected_result = self.Negnumber_1 / self.number_2
        self.assertEqual(result, expected_result)
        
    def test_Div_Positive_By_Negative(self):
        result = div(self.number_1, self.Negnumber_2)
        expected_result = self.number_1 / self.Negnumber_2
        self.assertEqual(result, expected_result)
    
    def test_Div_Negative_By_Negative(self):
        result = div(self.Negnumber_1, self.Negnumber_2)
        expected_result = self.Negnumber_1 / self.Negnumber_2
        self.assertEqual(result, expected_result)
    
    def test_Div_By_Decimal(self):
        result = div(self.number_1, self.Decimal_2)
        expected_result = round((self.number_1 / self.Decimal_2), 10)
        self.assertEqual(result, expected_result)
    
    def test_Div_Big_By_Small(self):
        result = div(self.a, self.small)
        expected_result = self.a / self.small
        self.assertEqual(result, expected_result)
    
    def test_Div_Small_By_Big(self):
        result = div(self.small, self.b)
        expected_result = self.small / self.b
        self.assertAlmostEqual(result, expected_result, places=2)
    
    def test_Div_Zero_By_NoneZero(self):
        result = div(0, self.number_1)
        self.assertEqual(result, 0)
    
    def test_Div_Float_By_Int(self):
        result = div(self.Decimal_1, self.number_1)
        expected_result = round((self.Decimal_1 / self.number_1), 10)
        self.assertEqual(result, expected_result)
    
    def test_Div_Int_By_Float(self):
        result = div(self.number_1, self.Decimal_1)
        expected_result = self.number_1 / self.Decimal_1
        self.assertEqual(result, expected_result)
    
    def test_Div_LargeNumbers(self):
        result = div(self.a, self.b)
        expected_result = self.a / self.b
        self.assertAlmostEqual(result, expected_result, places=2)
        
        

# @brief Tests of function factorial()        
class TestCalculator_factorial(unittest.TestCase):

    def setUp(self):
        self.a = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        self.test_nums = [
            (0, 1),
            (1, 1),
            (5, 120),
            (10, 3628800),
            (50, 30414093201713378043612608166064768844377641568960512000000000000)
        ]
    
    def test_Fac_InputExists(self):            
        self.assertIsNotNone(self.a)  
        with self.assertRaises(TypeError, msg="Test for empty input failed: Input is not None"):
            factorial()
            factorial('')
            factorial("")
            factorial(None)    
    
    def test_Fac_Is_Int(self):                      
       self.assertIsInstance(self.a, int)  
       for n, _ in self.test_nums:
            self.assertIsInstance(n, int)

    def test_Returns_Factorial(self):         
        for n, expected_result in self.test_nums:
            self.assertEqual(factorial(n), expected_result)
    
    def test_Fac_LargeNumbers(self):
        try:
            factorial(10000)
        except RecursionError:
            self.assertTrue(True)



# @brief Tests of function exponentiation()
class TestCalculator_exponents(unittest.TestCase):

    def setUp(self):
        self.number_1 = 5
        self.number_2 = 2
        self.Negnumber_1 = -5
        self.Negnumber_2 = -2
        self.Decimal_1 = 0.5
        self.a = 1000
        self.b = 9999
    
    def test_Exp_InputExists(self):            
        self.assertIsNotNone(self.number_1)
        self.assertIsNotNone(self.number_2)
        self.assertIsNotNone(self.Negnumber_1)
        self.assertIsNotNone(self.Negnumber_2)
        self.assertIsNotNone(self.a)
        self.assertIsNotNone(self.b)
    
    def test_Exp_NumberType(self):              
        self.assertIsInstance(self.number_1, int)
        self.assertIsInstance(self.number_2, int)
        self.assertIsInstance(self.Negnumber_1, int)
        self.assertIsInstance(self.Negnumber_2, int)
    
        self.assertIsInstance(self.a, int)
        self.assertIsInstance(self.b, int)
    
    def test_Returns_Exponent(self):         
        result = exponentiation(self.number_1, self.number_2)
        expected_result = self.number_1 ** self.number_2
        self.assertEqual(result, expected_result)
    
    def test_Exp_Decimal(self):
        result = exponentiation(self.number_1, self.Decimal_1)
        expected_result = round((self.number_1 ** self.Decimal_1), 10)  
        self.assertEqual(result, expected_result)
    
    def test_Exp_Large(self):
        expected_result = self.number_1 ** self.a
        self.assertEqual(exponentiation(self.number_1, self.a), expected_result)
    
    def test_Exp_Zero(self):
        self.assertEqual(exponentiation(0, 0), 1)
        self.assertEqual(exponentiation(self.number_1, 0), 1)
    
    def test_Exp_One(self):
        result = exponentiation(self.number_1, 1)
        self.assertEqual(result, self.number_1)
        
        
# @brief Tests of function sqrt()      
class TestCalculator_square_root(unittest.TestCase):

    def setUp(self):
        self.number_1 = 5 
        self.number_2 = 9
        self.Negnumber_1 = -5
        self.Negnumber_2 = -9
        self.Decimal_1 = 2.5

        self.a = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        self.b = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    
    def test_Sqrt_InputExists(self):
        self.assertIsNotNone(self.number_1)
        self.assertIsNotNone(self.number_2)
        self.assertIsNotNone(self.Negnumber_1)
        self.assertIsNotNone(self.Negnumber_2)
        self.assertIsNotNone(self.Decimal_1)
        self.assertIsNotNone(self.a)
        self.assertIsNotNone(self.b)
    
    def test_Sqrt_NumberType(self):
        self.assertIsInstance(self.number_1, (int, float))
        self.assertIsInstance(self.number_2, (int, float))
        self.assertIsInstance(self.Negnumber_1, (int, float))
        self.assertIsInstance(self.Negnumber_2, (int, float))
        self.assertIsInstance(self.Decimal_1, (int, float))
        self.assertIsInstance(self.a, (int, float))
        self.assertIsInstance(self.b, (int, float))

    def test_ReturnsSquare(self):
        result = sqrt(self.number_2)
        expected_result = math.sqrt(self.number_2)
        self.assertEqual(result, expected_result)
    
    def test_Sqrt_Noninteger(self):
        result = sqrt(self.Decimal_1)
        expected_result = math.sqrt(self.Decimal_1)
        self.assertAlmostEqual(result, expected_result)
    
    def test_Sqrt_Large(self):
        result = sqrt(self.a)
        expected_result = math.sqrt(self.a)
        self.assertAlmostEqual(result, expected_result)
   
    def test_Sqrt_Zero(self):
         self.assertEqual(sqrt(0), 0)
    
    def test_Sqrt_One(self):
        self.assertEqual(sqrt(1), 1)
    
    
# @brief Tests of function abs()   
class TestCalculator_absolute_value(unittest.TestCase):

    def setUp(self):
        self.number_1 = 5 
        self.Negnumber_1 = -5
        self.Decimal_1 = 2.5
        self.NegDecimal_1 = 2.5
        self.a = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        self.b = -10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    
    def test_Mod_InputExists(self):
        self.assertIsNotNone(self.number_1)
        self.assertIsNotNone(self.Negnumber_1)
        self.assertIsNotNone(self.Decimal_1)
        self.assertIsNotNone(self.NegDecimal_1)
        self.assertIsNotNone(self.a)
        self.assertIsNotNone(self.b)
    
    def test_Mod_NumberType(self):
        self.assertIsInstance(self.number_1, (int, float))
        self.assertIsInstance(self.Negnumber_1, (int, float))
        self.assertIsInstance(self.Decimal_1, (int, float))
        self.assertIsInstance(self.NegDecimal_1, (int, float))
        self.assertIsInstance(self.a, (int, float))
        self.assertIsInstance(self.b, (int, float))

    def test_ReturnsModulus(self):
        result = abs(self.number_1)
        expected_result = abs(self.number_1)
        self.assertEqual(result, expected_result)
    
    def test_Mod_Positive(self):
        self.assertEqual(abs(self.number_1), self.number_1)
    
    def test_Mod_Negative(self):
        self.assertEqual(abs(self.Negnumber_1), self.number_1)
    
    def test_Mod_Decimal_Negative(self):
        self.assertEqual(abs(self.NegDecimal_1), self.Decimal_1)
    
    def test_Mod_Decimal_Positive(self):
        self.assertEqual(abs(self.Decimal_1), self.Decimal_1)
    
    def test_Mod_Large(self):
        self.assertEqual(abs(self.b), self.a)
    
    def test_Mod_Zero(self):
        self.assertEqual(abs(0), 0)


if __name__ == "__main__":
    unittest.main()
