'''
Objective: To practice basic arithmetic operations in Python by performing predefined calculations.

Task Description:

You are required to complete a Python script that performs basic arithmetic operations with two predefined numbers. The script should do the following:

Assign specific values to two variables, number1 and number2.
Perform addition, subtraction, and multiplication on these numbers.
Print the results of these operations in a human-readable format.
Instructions:

Create a file named basic_operations.py.
In this file, you will define two variables: number1 and number2, with the values 10 and 5, respectively.
You do not need to write any functions or import any modules.
Calculate the sum, difference (by subtracting number2 from number1), and product of number1 and number2.
Print the results of each operation in the format: [operation] of [number1] and [number2] is [result].
Expected Output:

When executed, your script should print the following (assuming number1 = 10 and number2 = 5):

How to execute

python3 basic_operations.py
Here is the outcome

Addition of 10 and 5 is 15
Subtraction of 10 and 5 is 5
Multiplication of 10 and 5 is 50
Repo:

GitHub repository: alx_be_python
Directory: python_introduction
File: basic_operations.py
'''
number1 = 10
number2 =5
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 * number2
print(f"Addition of {number1} and {number2} is {addition}.")
print(f"Subtraction of {number1} and {number2} is {subtraction}.")
print(f"Multiplication of {number1} and {number2} is {multiplication}.")
print(f"Division of {number1} and {number2} is {division}.")