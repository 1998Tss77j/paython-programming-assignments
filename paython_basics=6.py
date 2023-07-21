# -*- coding: utf-8 -*-
"""paython basics=6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c8DXR1iiP7owWQZPADWotVFtfW8Sy2_E

1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
"""

def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def display_fibonacci_sequence(count):
    if count <= 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        print("Fibonacci Sequence:")
        for i in range(1, count + 1):
            print(fibonacci_recursive(i), end=", ")

# Example usage:
try:
    n = int(input("Enter the number of Fibonacci terms you want to display: "))
    display_fibonacci_sequence(n)
except ValueError:
    print("Invalid input. Please enter a positive integer.")

"""2. Write a Python Program to Find Factorial of Number Using Recursion?"""

def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

try:
    num = int(input("Enter a non-negative integer to find its factorial: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial_recursive(num)
        print(f"The factorial of {num} is: {result}")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")

"""3. Write a Python Program to calculate your Body Mass Index?"""

def calculate_bmi(weight, height):
    # Check for valid inputs
    if weight <= 0 or height <= 0:
        return "Invalid input. Weight and height must be positive numbers."

    # Calculate BMI
    bmi = weight / (height ** 2)
    return bmi

try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)

    print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numbers for weight and height.")

"""4. Write a Python Program to calculate the natural logarithm of any number?"""

import math

def calculate_natural_log(number):
    if number <= 0:
        return "Invalid input. The number must be a positive real number."

    return math.log(number)

try:
    num = float(input("Enter a positive real number to calculate its natural logarithm: "))
    result = calculate_natural_log(num)
    print(f"The natural logarithm of {num} is: {result:.2f}")
except ValueError:
    print("Invalid input. Please enter a positive real number.")

"""5. Write a Python Program for cube sum of first n natural numbers?"""

def cube_sum_of_natural_numbers(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."

    cube_sum = sum(i**3 for i in range(1, n+1))
    return cube_sum

try:
    num = int(input("Enter a positive integer (n) to calculate the cube sum of the first n natural numbers: "))
    result = cube_sum_of_natural_numbers(num)
    print(f"The cube sum of the first {num} natural numbers is: {result}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")