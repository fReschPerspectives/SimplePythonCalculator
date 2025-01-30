import unittest
from unittest.mock import patch, MagicMock
from SimplePythonCalculator import CalculatorFunctions as cf
from SimplePythonCalculator.Calculator import CALC, get_entry_value, entry_update, equal_entries, perform_operation, equals
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

class TestCalculator(unittest.TestCase):

    CALC = cf.Calculator()

    @patch('SimplePythonCalculator.Calculator.result')
    def test_get_entry_value(self, mock_result):
        mock_result.get.return_value = '5.0'
        get_entry_value()
        self.assertEqual(CALC.input_value, 5.0)


    @patch('SimplePythonCalculator.Calculator.result')
    def test_add_equal_entries(self, mock_result):
        mock_result.get.return_value = '5.0'
        CALC.procedure = 'add'
        CALC.current_value = 5.0
        CALC.input_value = 5.0
        equal_entries()
        self.assertEqual(CALC.current_value, 10.0)

    @patch('SimplePythonCalculator.Calculator.result')
    def test_multiply_equal_entries(self, mock_result):
        mock_result.get.return_value = '5.0'
        CALC.procedure = 'multiply'
        CALC.current_value = 5.0
        CALC.input_value = 5.0
        equal_entries()
        self.assertEqual(CALC.current_value, 25.0)

    @patch('SimplePythonCalculator.Calculator.result')
    def test_divide_equal_entries(self, mock_result):
        mock_result.get.return_value = '5.0'
        CALC.procedure = 'divide'
        CALC.current_value = 5.0
        CALC.input_value = 5.0
        equal_entries()
        self.assertEqual(CALC.current_value, 1.0)

    @patch('SimplePythonCalculator.Calculator.result')
    def test_subtraction_equal_entries(self, mock_result):
        mock_result.get.return_value = '5.0'
        CALC.procedure = 'subtract'
        CALC.current_value = 5.0
        CALC.input_value = 5.0
        equal_entries()
        self.assertEqual(CALC.current_value, 0.0)


    @patch('SimplePythonCalculator.Calculator.result')
    def test_perform_operation(self, mock_result):
        CALC.current_value = 0.0
        CALC.input_value = 5.0
        CALC.lock = False
        mock_result.get.return_value = '5.0'
        perform_operation('add')
        self.assertEqual(CALC.procedure, 'add')
        self.assertEqual(CALC.current_value, 5.0)

    @patch('SimplePythonCalculator.Calculator.result')
    def test_equals(self, mock_result):
        mock_result.get.return_value = '5.0'
        CALC.procedure = 'add'
        CALC.current_value = 5.0
        CALC.input_value = 5.0
        equals()
        self.assertEqual(CALC.final_value, 10.0)
        self.assertTrue(CALC.init_state)
        self.assertTrue(CALC.refresh_screen)


if __name__ == '__main__':
    unittest.main()