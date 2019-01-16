# =========================================
# use python test_calculator.py -v
# to run tests
# =========================================

import unittest
import sys
sys.path.append('../')
from calculator import Calculator

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
    

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    self.assertEqual(self.calc.add(2, 7), 9)

  # Write test methods for subtract, multiply, and divide

  def test_subtract(self):
    self.assertEqual(self.calc.subtract(7, 2), 5)

  def test_multiply(self):
    self.assertEqual(self.calc.multiply(2,10), 20)

  def test_divide(self):
    self.assertEqual(self.calc.divide(25,5), 5)

    

if __name__ == '__main__':
    unittest.main()