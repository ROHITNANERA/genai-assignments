"""
Task 3: discount.py inside shop_package
"""

def apply_discount(price, percent):
    return price - (price * (percent / 100))

def flat_discount(price):
    return price - 50

if __name__ == "__main__":
    print(f"apply_discount(100, 20): {apply_discount(100, 20)}")
    print(f"flat_discount(100): {flat_discount(100)}")

"""
Example Output:
apply_discount(100, 20): 80.0
flat_discount(100): 50
"""
