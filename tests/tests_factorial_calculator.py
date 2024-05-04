import unittest
from factorial_calculator import calculate_factorial

class TestFactorialCalculator(unittest.TestCase):

    def test_calculate_factorial(self):
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)
        self.assertEqual(calculate_factorial(2), 2)
        self.assertEqual(calculate_factorial(5), 120)
        # Add more test cases as needed

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-1)

if __name__ == '__main__':
    unittest.main()
