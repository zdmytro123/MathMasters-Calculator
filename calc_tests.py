import unittest
import math

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

class TestsCalculator_addition(unittest.TestCase):
    def setUp(self):
        self.number_1 = 1
        self.number_2 = 2
        self.number_3 = 3     
        self.number_4 = 1.4573534
        self.number_5 = 2.3465463
        self.number_6 = -234
        self.number_7 = -85
        self.a = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        self.b = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    #1
    def test_InputExists(self):             #if input not NULL
        self.assertIsNotNone(self.number_1)
        self.assertIsNotNone(self.number_2)
    #2
    def test_NumberType(self):              #if it is a number
        self.assertIsInstance(self.number_1, (int, float))
        self.assertIsInstance(self.number_1, (int, float))
    #3
    def test_ReturnsAddition(self):         #if it returns addition
        result = add(self.number_1, self.number_2)
        excepted_result = self.number_1 + self.number_2
        self.assertEqual(result, excepted_result)
    #4
    def test_Commutativity(self):           #if add(a, b) returns the same result as add(b, a)
        result1 = add(self.number_1, self.number_2)
        result2 = add(self.number_2, self.number_1)
        self.assertEqual(result1, result2)
    #5
    def test_associativity(self):           #if add(a, add(b, c)) returns the same result as add(add(a, b), c)
        result1 = add(self.number_1, add(self.number_2, self.number_3))
        result2 = add(add(self.number_1, self.number_2), self.number_3)
        self.assertEqual(result1, result2)
    #6    
    def test_identity(self):                # Adding 0 to a number should not change the value of the number
        result = add(self.number_1, 9)
        self.assertEqual(result, self.number_1)
    #7
    def test_AddLargeNumbers(self):
        result1 = add(self.a, self.b)
        result2 = self.a + self.b
        self.assertEqual(result1, result2)
    #8
    def test_AddDecimalNumbers(self):          #testing for decimal numbers  
        result1 = add(self.number_4, self.number_5)
        result2 = self.number_4 + self.number_5
        self.assertAlmostEqual(result1, result2, places=2) #places погрешность цифр после запятой (у нас 10**2)
    #9
    def test_AddTwoNegativNumbers(self):            #addition of two negative numbers
        result = add(self.number_6, self.number_7)
        excepted_result = self.number_6 + self.number_7
        self.assertEqual(result, excepted_result)
    #10
    def test_AddNegativeToPositive(self):        #addition of negative numbers to positive
        result = add(self.number_6, self.number_3)
        excepted_result = self.number_6 + self.number_3
        self.assertEqual(result, excepted_result)
    #11
    # def test_ComplexNumbers(args):
        

    
class TestsCalculator_substraction(unittest.TestCase):
    def setUp(self):
        self.number_1 = 5
        self.number_2 = 1
        self.number_3 = -23
        self.number_4 = 6.789
        self.number_5 = 1.5
        self.number_6 = 3+4j
        self.number_7 = 1-8j
        self.a = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        self.b = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    #1
    def test_InputExists(self):                 #if input not NULL
        self.assertIsNotNone(self.number_1)
        self.assertIsNotNone(self.number_2)
    #2
    def test_NumberType(self):                  #if it is a number
        self.assertIsInstance(self.number_1, (int, float, complex))
        self.assertIsInstance(self.number_1, (int, float, complex))
    #3
    def test_ReturnsSubstraction(self):         #if it returns addition
        result = sub(self.number_1, self.number_2)
        excepted_result = self.number_1 - self.number_2
        self.assertEqual(result, excepted_result)
    #4
    def test_SubTwoNegativNumbers(self):            #subtraction of two negative numbers
        result = sub(self.number_3, self.number_4)
        excepted_result = self.number_3 - self.number_4
        self.assertEqual(result, excepted_result)
    #5
    def test_SubNegativeFromPositive(self):        #subtraction of negative numbers from positive
        result = sub(self.number_1, self.number_3)
        excepted_result = self.number_1 - self.number_3
        self.assertEqual(result, excepted_result)
    #6
    def test_SubPositiveFromNegative(self):        #subtraction of positive number from negative 
        result = sub(self.number_3, self.number_1)
        excepted_result = self.number_3 - self.number_1
        self.assertEqual(result, excepted_result)
    #7
    def test_SubLargeNumbers(self):
        result1 = sub(self.a, self.b)
        result2 = self.a - self.b
        self.assertEqual(result1, result2)
    #8
    def test_SubtTwoDecimalNumbers(self):
        result = sub(self.number_4, self.number_5)
        excepted_result = self.number_4 - self.number_5
        self.assertAlmostEqual(result, excepted_result, places=2)
    #9
    # def test_SubtractTwoComplexNumbers(self):
    #     result = sub(self.number_6, self.number_7)
    #     self.assertAlmostEqual(result.real, 2.0, places=2)
    #     self.assertAlmostEqual(result.imag, 3.0, places=2)
    #10
    def test_identity(self):  
        result = sub(self.number_1, 0)
        self.assertEqual(result, self.number_1)


if __name__ == "__main__":
    unittest.main()