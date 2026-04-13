"""
Task 1: math_utils.py
Create a simple module with basic math operations.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def square(n):
    return n ** 2

if __name__ == "__main__":
    print(f"add(5, 3): {add(5, 3)}")
    print(f"subtract(10, 4): {subtract(10, 4)}")
    print(f"square(6): {square(6)}")

"""
Example Output:
add(5, 3): 8
subtract(10, 4): 6
square(6): 36
"""
