import unittest

class Calculator:
  def __init__(self,x1,x2):
    self.x1 = x1
    self.x2 = x2
  def add(self):
    return self.x1 + self.x2
  def multiply(self):
    return self.x1 * self.x2
  def subtract(self):
    return self.x1 - self.x2
  def divide(self):
    if self.x1 != 0:
      return self.x1/self.x2

class TestCalculator(unittest.TestCase):
  def setUp(self):
    self.calculator = Calculator(float(input('\nWrite x1\n')), float(input('\nWrite x2\n')))
  def test_add(self):
    self.assertEqual(self.calculator.add(), 11)

  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(), 5)

  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(), 21)
    
  def test_divide(self):
    self.assertEqual(self.calculator.divide(), 5)
if __name__ == "__main__":
  unittest.main(verbosity=2)