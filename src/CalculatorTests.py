import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(2, 2), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_square_root_method_calculator(self):
        self.assertEqual(2, self.calculator.square_root(4))
        self.assertEqual(0, self.calculator.square_root(0))
        self.assertEqual("nan", self.calculator.square_root(-4))

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(2), 4)
        self.assertEqual(self.calculator.result, 4)


if __name__ == '__main__':
    unittest.main()
