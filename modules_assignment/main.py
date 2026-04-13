"""
Task 4: main.py
Main testing script connecting all modules and shop_package.
"""

# Task 1 Imports
import math_utils
from math_utils import square

# Task 2 Imports
import string_utils

# Task 4 Imports for shop_package
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax

def main():
    print("=== Testing math_utils ===")
    print(f"math_utils.add(10, 5): {math_utils.add(10, 5)}")
    print(f"math_utils.subtract(20, 8): {math_utils.subtract(20, 8)}")
    print(f"square(7) using 'from import': {square(7)}")

    print("\n=== Testing string_utils ===")
    text = "python modules are fun"
    print(f"Original Text: {text}")
    print(f"capitalized: {string_utils.capitalize_words(text)}")
    print(f"reversed: {string_utils.reverse_string(text)}")
    print(f"word count: {string_utils.word_count(text)}")

    print("\n=== Testing shop_package ===")
    print(f"disc.apply_discount(1000, 10): {disc.apply_discount(1000, 10)}")
    print(f"disc.flat_discount(500): {disc.flat_discount(500)}")
    
    prices = [100, 200, 300, 400]
    total = calculate_total(prices)
    print(f"calculate_total(prices): {total}")
    print(f"apply_tax(total): {apply_tax(total)}")

if __name__ == "__main__":
    main()

"""
Example Output:
=== Testing math_utils ===
math_utils.add(10, 5): 15
math_utils.subtract(20, 8): 12
square(7) using 'from import': 49

=== Testing string_utils ===
Original Text: python modules are fun
capitalized: Python Modules Are Fun
reversed: nuf era seludom nohtyp
word count: 4

=== Testing shop_package ===
disc.apply_discount(1000, 10): 900.0
disc.flat_discount(500): 450
calculate_total(prices): 1000
apply_tax(total): 1050.0
"""
