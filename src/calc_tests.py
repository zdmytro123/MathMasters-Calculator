import unittest
import math

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ZeroDivisionError("Error: division by zero")
    else:
        return x / y
    

    
#other tests: Order of operations(e.g., multiplication before addition). 
#             Memory: Test that the calculator can store and recall values from memory, if calculator supports this feature.
#             Three negative numbers

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
    def test_AddInputExists(self):             #if input not NULL
        self.assertIsNotNone(self.number_1)
        self.assertIsNotNone(self.number_2)
        self.assertIsNotNone(self.number_3)
        self.assertIsNotNone(self.number_4)
        self.assertIsNotNone(self.number_5)
        self.assertIsNotNone(self.number_6)
        self.assertIsNotNone(self.number_7)
        self.assertIsNotNone(self.a)
        self.assertIsNotNone(self.b)
    #2
    def test_AddNumberType(self):              #if it is a number
        self.assertIsInstance(self.number_1, (int, float))
        self.assertIsInstance(self.number_2, (int, float))
        self.assertIsInstance(self.number_3, (int, float))
        self.assertIsInstance(self.number_4, (int, float))
        self.assertIsInstance(self.number_5, (int, float))
        self.assertIsInstance(self.number_6, (int, float))
        self.assertIsInstance(self.number_7, (int, float))
        self.assertIsInstance(self.a, (int, float))
        self.assertIsInstance(self.b, (int, float))
    #3
    def test_ReturnsAddition(self):         #if it returns addition
        result = add(self.number_1, self.number_2)
        excepted_result = self.number_1 + self.number_2
        self.assertEqual(result, excepted_result)
    #4
    def test_AddCommutativity(self):           #if add(a, b) returns the same result as add(b, a)
        result1 = add(self.number_1, self.number_2)
        result2 = add(self.number_2, self.number_1)
        self.assertEqual(result1, result2)
    #5
    def test_AddAssociativity(self):           #if add(a, add(b, c)) returns the same result as add(add(a, b), c)
        result1 = add(self.number_1, add(self.number_2, self.number_3))
        result2 = add(add(self.number_1, self.number_2), self.number_3)
        self.assertEqual(result1, result2)
    #6    
    def test_AddIdentity(self):                # Adding 0 to a number should not change the value of the number
        result = add(self.number_1, 0)
        self.assertEqual(result, self.number_1, "adding 0 to a number changed the value of the number")
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
    def test_AddTwoNegativeNumbers(self):            #addition of two negative numbers
        result = add(self.number_6, self.number_7)
        excepted_result = self.number_6 + self.number_7
        self.assertEqual(result, excepted_result)
    #10
    def test_AddNegativeToPositive(self):        #addition of negative numbers to positive
        result = add(self.number_6, self.number_3)
        excepted_result = self.number_6 + self.number_3
        self.assertEqual(result, excepted_result)
    
class TestsCalculator_substraction(unittest.TestCase):
    def setUp(self):
        self.number_1 = 5
        self.number_2 = 1
        self.number_3 = -23
        self.number_4 = 6.789
        self.number_5 = 1.5
        self.a = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        self.b = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    #1
    def test_SubInputExists(self):                 #if input not NULL
        self.assertIsNotNone(self.number_1)
        self.assertIsNotNone(self.number_2)
        self.assertIsNotNone(self.number_3)
        self.assertIsNotNone(self.number_4)
        self.assertIsNotNone(self.number_5)
        self.assertIsNotNone(self.a)
        self.assertIsNotNone(self.b)
    #2
    def test_SubNumberType(self):                  #if it is a number
        self.assertIsInstance(self.number_1, (int, float))
        self.assertIsInstance(self.number_2, (int, float))
        self.assertIsInstance(self.number_3, (int, float))
        self.assertIsInstance(self.number_4, (int, float))
        self.assertIsInstance(self.number_5, (int, float))
        self.assertIsInstance(self.a, (int, float))
        self.assertIsInstance(self.b, (int, float))
    #3
    def test_ReturnsSubstraction(self):         #if it returns addition
        result = sub(self.number_1, self.number_2)
        excepted_result = self.number_1 - self.number_2
        self.assertEqual(result, excepted_result)
    #4
    def test_SubTNegativNumbers(self):            #subtraction of two negative numbers
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
    def test_SubIdentity(self):  
        result = sub(self.number_1, 0)
        self.assertEqual(result, self.number_1)

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
    #1
    def test_MulInputExists(self):
        self.assertIsNotNone(self.number_1)
        self.assertIsNotNone(self.number_2)
        self.assertIsNotNone(self.Negnumber_1)
        self.assertIsNotNone(self.Negnumber_2)
        self.assertIsNotNone(self.Decimal_1)
        self.assertIsNotNone(self.Decimal_2)
        self.assertIsNotNone(self.a)
        self.assertIsNotNone(self.b)
    #2
    def test_MulNumberType(self):
        self.assertIsInstance(self.number_1, (int, float))
        self.assertIsInstance(self.number_2, (int, float))
        self.assertIsInstance(self.Negnumber_1, (int, float))
        self.assertIsInstance(self.Negnumber_2, (int, float))
        self.assertIsInstance(self.Decimal_1, (int, float))
        self.assertIsInstance(self.Decimal_2, (int, float))
        self.assertIsInstance(self.a, (int, float))
        self.assertIsInstance(self.b, (int, float))

    #3
    def test_ReturnsMultiplication(self):
        result = (mul(self.number_1, self.number_2))
        excepted_result = self.number_1 * self.number_2
        self.assertEqual(result, excepted_result)
    #4
    def test_MulCommutativity(self):           #if mul(a, b) returns the same result as mul(b, a)
        result1 = mul(self.number_1, self.number_2)
        result2 = mul(self.number_2, self.number_1)
        self.assertEqual(result1, result2)
    #5
    def test_MulIdentity(self):                # multiplication 1 to a number should not change the value of the number
        result = mul(self.number_1, 1)
        self.assertEqual(result, self.number_1, "multiplication 1 changed value")
    #6
    def test_MulZero(self):
        result = mul(self.number_1, 0)
        self.assertEqual(result, 0, "multiplication 0 returned non-zero number")
    #7
    def test_MulTwoNegativeNumbers(self):
        result = mul(self.Negnumber_1, self.Negnumber_2)
        excepted_result = self.Negnumber_1 * self.Negnumber_2
        self.assertEqual(result, excepted_result)
    #8
    def test_MulNegativeAndPositiveNumbers(self):
        result = mul(self.Negnumber_1, self.number_2)
        excepted_result = self.Negnumber_1 * self.number_2
        self.assertEqual(result, excepted_result)
    #9
    def test_MulTwoDecimalNumbers(self):
        result = mul(self.Decimal_1, self.Decimal_2)
        excepted_result = self.Decimal_1 * self.Decimal_2
        self.assertAlmostEqual(result, excepted_result, places=2)
    #10
    def test_MulDecimalAndZero(self):
        result = mul(self.Decimal_1, 0)
        self.assertEqual(result, 0)
    #11
    def test_MulLargeNumbers(self):
        result1 = mul(self.a, self.b)
        result2 = self.a * self.b
        self.assertEqual(result1, result2)
    
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
    #1
    def test_DivInputExists(self):             #if input not NULL
        self.assertIsNotNone(self.number_1)
        self.assertIsNotNone(self.number_2)
    #2
    def test_DivNumberType(self):              #if it is a number
        self.assertIsInstance(self.number_1, (int, float))
        self.assertIsInstance(self.number_2, (int, float))
    #3
    def test_ReturnsDivision(self):         #if it returns addition
        result = div(self.number_1, self.number_2)
        excepted_result = self.number_1 / self.number_2
        self.assertEqual(result, excepted_result)
    #4
    def test_IntegerDivision(self):
        result = div(self.number_1, self.number_2)
        excepted_result = self.number_1 / self.number_2
        self.assertEqual(result, excepted_result)
    #5
    def test_FloatDivision(self):
        result = div(self.Decimal_1, self.Decimal_2)
        excepted_result = self.Decimal_1 / self.Decimal_2
        self.assertAlmostEqual(result, excepted_result, places=2)
    #???????????????????????????????????????????????????????????????????????????????????????????????????????????
    def test_ZeroDivision(self):
        try:
            div(self.number_1, 0)
            self.fail("Expected Division by zero")
        except ZeroDivisionError:
            pass
    #7
    def test_NegativeByPositive(self):
        result = div(self.Negnumber_1, self.number_2)
        excepted_result = self.Negnumber_1 / self.number_2
        self.assertEqual(result, excepted_result)
    #8    
    def test_PositiveByNegative(self):
        result = div(self.number_1, self.Negnumber_2)
        excepted_result = self.number_1 / self.Negnumber_2
        self.assertEqual(result, excepted_result)
    #9
    def test_NegativeByNegative(self):
        result = div(self.Negnumber_1, self.Negnumber_2)
        excepted_result = self.Negnumber_1 / self.Negnumber_2
        self.assertEqual(result, excepted_result)
    #10
    def test_DivByDecimal(self):
        result = div(self.number_1, self.Decimal_2)
        excepted_result = self.number_1 / self.Decimal_2
        self.assertEqual(result, excepted_result)
    #11
    def test_DivBigBySmall(self):
        result = div(self.a, self.small)
        excepted_result = self.a / self.small
        self.assertEqual(result, excepted_result)
    #12
    def test_DivSmallByBig(self):
        result = div(self.small, self.b)
        excepted_result = self.small / self.b
        self.assertAlmostEqual(result, excepted_result, places=2)
    #13
    def test_ZeroByNoneZero(self):
        result = div(0, self.number_1)
        self.assertEqual(result, 0)
    #14
    #tut napsal decimal misto float
    def test_FloatByInt(self):
        result = div(self.Decimal_1, self.number_1)
        excepted_result = self.Decimal_1 / self.number_1
        self.assertEqual(result, excepted_result)
    #15
    def test_IntByFloat(self):
        result = div(self.number_1, self.Decimal_1)
        excepted_result = self.number_1 / self.Decimal_1
        self.assertEqual(result, excepted_result)
    #16
    def test_DivLargeNumbers(self):
        result = div(self.a, self.b)
        excepted_result = self.a / self.b
        self.assertAlmostEqual(result, excepted_result, places=2)
        


if __name__ == "__main__":
    unittest.main()