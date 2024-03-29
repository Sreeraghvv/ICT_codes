# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QqB1wB8RdFTUuDBBrD_aew34b-bcBDou
"""



class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        else:
            return x / y

    def calculate(self, x, y, operator):
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

        if operator in operations:
            return operations[operator](x, y)
        else:
            return "Invalid operator"


if __name__ == "__main__":
    calculator = Calculator()
    while True:
        try:
            expression = input("Enter expression (e.g., 5 + 3): (or 'exit' to quit): ")
            if expression.lower() == 'exit':
                break

            parts = expression.split()
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            result = calculator.calculate(num1, num2, operator)
            print("Result:", result)
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid expression.")
