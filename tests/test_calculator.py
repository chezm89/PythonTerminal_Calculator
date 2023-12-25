import unittest
from pythonCode import calculator

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        
        self.assertEqual(calculator.add(10,5), 15)
        self.assertEqual(calculator.add(-10,-5), -15)
        self.assertEqual(calculator.add(-10,5), -5)
        
    def test_subtract(self):
        
        self.assertEqual(calculator.subtract(10,5), 5)
        self.assertEqual(calculator.subtract(-10,-5), -5)
        self.assertEqual(calculator.subtract(-10,5), -15)
    
    def test_multiply(self):
        
        self.assertEqual(calculator.multiply(10,5), 50)
        self.assertEqual(calculator.multiply(-10,-5), 50)
        self.assertEqual(calculator.multiply(-10,5), -50)
    
    def test_divide(self):
        
        self.assertEqual(calculator.divide(10,5), 2)
        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide(-1,-1), 1)
        self.assertEqual(calculator.divide(5,2), 2.5)
        
        self.assertRaises(ValueError, calculator.divide, 10,0)
        
if __name__ == "__main__":
    unittest.main()