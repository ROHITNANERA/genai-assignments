"""
Task 2 - Recursive Function: Factorial Utility
Create a recursive function factorial(n) that:
1. Returns the factorial of n.
2. Handles two edge cases: n == 0 and n == 1.
3. Prints an error message if n is negative.
"""

def factorial(n: int) -> int | None:
    """
    Returns the factorial of a sequence recursively.
    Handles negative numbers by printing an error.
    """
    # Handle negative numbers
    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None
    
    # Base/Edge cases
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

# Test cases
if __name__ == "__main__":
    print(f"factorial(5): {factorial(5)}")
    print(f"factorial(0): {factorial(0)}")
    print(f"factorial(-3):")
    factorial(-3)

"""
Example Output:
factorial(5): 120
factorial(0): 1
factorial(-3):
Error: Factorial is not defined for negative numbers.
"""
