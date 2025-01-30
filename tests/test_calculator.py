import unittest
from unittest.mock import patch, MagicMock
from SimplePythonCalculator import CalculatorFunctions as cf
from SimplePythonCalculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = cf.Calculator()
        Calculator.CALC = self.calc

    @patch('Calculator.result')
    def test_get_entry_value(self, mock_result):
        mock_result.get.return_value = '5.0'
        Calculator.get_entry_value()
        self.assertEqual(self.calc.input_value, 5.0)

    @patch('Calculator.result')
    def test_entry_update(self, mock_result):
        mock_result.get.return_value = '0.0'
        Calculator.entry_update(value='7')
        mock_result.delete.assert_called_once_with(0, Calculator.tkinter.END)
        mock_result.insert.assert_called_once_with(0, '7')

    @patch('Calculator.result')
    def test_equal_entries(self, mock_result):
        self.calc.input_value = 5.0
        self.calc.current_value = 0.0
        self.calc.procedure = 'add'
        self.calc.lock = False
        Calculator.equal_entries()
        self.assertEqual(self.calc.current_value, 5.0)
        self.assertTrue(self.calc.lock)

    @patch('Calculator.result')
    def test_perform_operation(self, mock_result):
        self.calc.init_state = True
        self.calc.lock = False
        mock_result.get.return_value = '5.0'
        Calculator.perform_operation('add')
        self.assertEqual(self.calc.procedure, 'add')
        self.assertFalse(self.calc.init_state)
        self.assertTrue(self.calc.lock)

    @patch('Calculator.result')
    def test_equals(self, mock_result):
        self.calc.input_value = 5.0
        self.calc.current_value = 0.0
        self.calc.procedure = 'add'
        self.calc.lock = False
        Calculator.equals()
        self.assertFalse(self.calc.lock)
        self.assertTrue(self.calc.init_state)
        self.assertEqual(self.calc.current_value, 0.0)

if __name__ == '__main__':
    unittest.main()