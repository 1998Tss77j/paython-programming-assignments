# -*- coding: utf-8 -*-
"""paython basic assi=5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10CEaFZBQraHlLiNnFn3QcTIEmU6xRXWo

1. Write a Python Program to Find LCM?
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def find_lcm(numbers):
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to find LCM.")

    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

# Example usage:
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = find_lcm([num1, num2])
    print(f"The LCM of {num1} and {num2} is: {result}")
except ValueError as e:
    print(e)

"""2. Write a Python Program to Find HCF?"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_hcf(a, b):
    return gcd(a, b)

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = find_hcf(num1, num2)
    print(f"The HCF of {num1} and {num2} is: {result}")
except ValueError as e:
    print(e)

"""3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?"""

def decimal_to_binary(decimal_num):
    return bin(decimal_num).replace("0b", "")

def decimal_to_octal(decimal_num):
    return oct(decimal_num).replace("0o", "")

def decimal_to_hexadecimal(decimal_num):
    return hex(decimal_num).replace("0x", "").upper()

try:
    decimal_input = int(input("Enter a decimal number: "))

    binary_result = decimal_to_binary(decimal_input)
    octal_result = decimal_to_octal(decimal_input)
    hexadecimal_result = decimal_to_hexadecimal(decimal_input)

    print(f"Decimal {decimal_input} in Binary: {binary_result}")
    print(f"Decimal {decimal_input} in Octal: {octal_result}")
    print(f"Decimal {decimal_input} in Hexadecimal: {hexadecimal_result}")
except ValueError as e:
    print("Invalid input. Please enter a valid decimal number.")

"""4. Write a Python Program To Find ASCII value of a character?"""

try:
    char_input = input("Enter a character: ")

    if len(char_input) != 1:
        raise ValueError("Please enter a single character.")

    ascii_value = ord(char_input)
    print(f"The ASCII value of '{char_input}' is: {ascii_value}")
except ValueError as e:
    print(e)

"""5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?"""

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter the operation number (1/2/3/4): "))

    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)
    else:
        raise ValueError("Invalid choice. Please choose a valid operation number (1/2/3/4).")

    print(f"Result: {result}")
except ValueError as e:
    print(e)