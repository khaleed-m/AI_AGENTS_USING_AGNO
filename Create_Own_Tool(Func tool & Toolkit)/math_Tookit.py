from agno.tools import Toolkit

class MathToolkit(Toolkit):
    def __init__(self):
        super().__init__(name="math_toolkit")
        self.register(self.add_numbers)
        self.register(self.subtract_numbers)
        self.register(self.multiply_numbers)
        self.register(self.divide_numbers)

    def add_numbers(self, a: int, b: int) -> int:
        return (a + b)

    def subtract_numbers(self, a: int, b: int) -> int:
        return (a - b)

    def multiply_numbers(self, a: int, b: int) -> int:
        return (a * b)

    def divide_numbers(self, a: int, b: int) -> float:
        if b == 0:
            return "Error: Cannot divide by zero."
        return (a / b)
