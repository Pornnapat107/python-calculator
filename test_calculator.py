import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(self.calc.add(6, 2), 8)
        
    def test_delete(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_delete2(self):
        self.assertEqual(self.calc.subtract(8, 4), 4)
    
    def test_time(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_time2(self):
        self.assertEqual(self.calc.multiply(5, 6), 30)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_mod2(self):
        self.assertEqual(self.calc.modulo(10, 5), 0)

if __name__ == '__main__':
    unittest.main()