class MathOperations:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def add_numbers(self):
        return self.operand1 + self.operand2

    def concatenate_strings(self):
        return str(self.operand1) + str(self.operand2)

# Creating an instance of MathOperations class for adding numbers
math_operations_numbers = MathOperations(5, 3)

# Adding numbers using the add_numbers method
result_sum = math_operations_numbers.add_numbers()
print(f"The sum of numbers is: {result_sum}")

# Creating another instance of MathOperations class for concatenating strings
math_operations_strings = MathOperations("Hello", "World")

# Concatenating strings using the concatenate_strings method
result_concatenation = math_operations_strings.concatenate_strings()
print(f"The concatenated string is: {result_concatenation}")
