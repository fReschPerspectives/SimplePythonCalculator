"""
These are the functions needed for the basic calculator
GUI: basic arithmetic operations and display the results
"""

import typing

class Calculator:
    def __init__(self):
        self.init_state = True
        self.lock = False
        self.refresh_screen = False
        self.procedure = ""
        self.initial_value = 0.0
        self.input_value = 0.0
        self.current_value = 0.0
        self.final_value = 0.0

    def clear(self):
        self.current_value = 0
        return

    def add(self) -> None:
        current_value = self.current_value
        result = current_value + self.input_value
        self.current_value = result
        return

    def subtract(self) -> None:
        result = self.current_value - self.input_value
        self.current_value = result
        return

    def multiply(self) -> None:
        result = self.current_value * self.input_value
        self.current_value = result
        return

    def divide(self) -> None:
        if self.input_value == 0:
            self.current_value = 0.0
            return
        else:
            result = self.current_value / self.input_value
        self.current_value = result
        return

    def set_input_value(self, input_value: float) -> None:
        self.input_value = input_value
        return

    def set_final_value(self) -> float:
        self.final_value = self.current_value
        return

    def get_final_value(self) -> float:
        return self.final_value
        return

    def print_input_value(self)->None:
        print(self.input_value)
        return
