"""
Task 3: billing.py inside shop_package
"""

def calculate_total(prices):
    return sum(prices)

def apply_tax(amount):
    return amount + (amount * 0.05)

if __name__ == "__main__":
    prices = [100, 200, 300]
    total = calculate_total(prices)
    print(f"calculate_total([100, 200, 300]): {total}")
    print(f"apply_tax(total): {apply_tax(total)}")

"""
Example Output:
calculate_total([100, 200, 300]): 600
apply_tax(total): 630.0
"""
