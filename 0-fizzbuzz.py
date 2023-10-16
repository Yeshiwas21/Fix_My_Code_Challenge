#!/usr/bin/python3
"""
FizzBuzz: A program that prints numbers from 1 to n with specific rules.

This program prints numbers from 1 to n, following the FizzBuzz rules:
- For multiples of three, it prints "Fizz" instead of the number.
- For multiples of five, it prints "Buzz" instead of the number.
- For numbers that are multiples of both three and five, it prints "FizzBuzz."

Usage:
    ./fizzbuzz.py <number>

Example:
    ./fizzbuzz.py 15
"""

import sys

def fizzbuzz(n):
    """
    Print numbers from 1 to n according to FizzBuzz rules.

    Args:
        n (int): The maximum number to print up to (inclusive).

    Returns:
        None

    This function iterates from 1 to n and prints the numbers according to the FizzBuzz rules.
    """
    if n < 1:
        return

    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    print(" ".join(result))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./fizzbuzz.py <number>")
        print("Example: ./fizzbuzz.py 15")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        sys.exit(1)

    results = fizzbuzz(number)
    print(" ".join(results))
