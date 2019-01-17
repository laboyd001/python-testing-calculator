# =========================================
# use python test_calculator.py -v
# to run tests
# =========================================

import unittest
import sys
sys.path.append('../')
from calculator import Calculator


# setUpModule and tearDownModule are included with unit testing in python
# these are things that you just put in tests...  really for times when you have multiple test classes
def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    print('Set up class')
    # Create an instance of the calculator that can be used in all tests
    cls.calc = Calculator()
    cls.num1 = 2
    cls.num2 = 6
    

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    result = self.calc.add(2, 7)
    expected = 9
    print("result", result)
    print("expected", expected)
    self.assertEqual(result, expected)
    self.assertNotEqual(self.calc.add(3, 3), 4)
    self.assertEqual(self.calc.add(self.num1, self.num2), 8)




  # Write test methods for subtract, multiply, and divide

  def test_subtract(self):
    self.assertEqual(self.calc.subtract(7, 2), 5)

  def test_multiply(self):
    self.assertEqual(self.calc.multiply(2,10), 20)

  def test_divide(self):
    self.assertEqual(self.calc.divide(25,5), 5)

    

if __name__ == '__main__':
    unittest.main()