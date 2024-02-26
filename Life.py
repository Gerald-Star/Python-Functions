import math


theAnswer = 42
name = 'Softlinks'

number = 225
result = math.sqrt(number)

'''
User
import the math module, use the square root method in Python from math module, - create a function called square_root(),
that take one input and returns a square root, 
- calculate the square root of 225
'''


def square_root(number):
    """
    Use the python math module documentation
    Calculate the square root of a given number.

    Parameters:
        number (float or int): The number whose square root is to be calculated.

    Returns:
        float: The square root of the input number.
    """
    return math.sqrt(number)


# Calculate the square root of 225
result = square_root(225)
print("Square root of 225:", result)
