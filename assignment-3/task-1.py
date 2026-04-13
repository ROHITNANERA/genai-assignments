"""
Task 1 - Basic Function: Price After Discount
Write a function apply_discount(price, discount_percent) that:
1. Returns the price after discount.
2. If discount_percent is missing, apply a default discount of 5%.
Extra (optional): Add a condition inside the function to ensure discount never exceeds 60%.
"""

def apply_discount(price: float, discount_percent: float = 5) -> float:
    """
    Applies a discount to a given price and returns the new price.
    The discount_percent defaults to 5%.
    The discount_percent is capped at a maximum of 60%.
    """
    # Restrict maximum discount to 60%
    if discount_percent > 60:
        print("Warning: Discount exceeds 60%. Capping at 60%.")
        discount_percent = 60
    
    # Calculate the discount amount
    discount_amount = (price * discount_percent) / 100
    
    # Return the final price after discount
    return price - discount_amount


# Test the function with example inputs
if __name__ == "__main__":
    print(f"Price after 10% discount on 1000: {apply_discount(1000, 10)}")
    print(f"Price after default discount on 500: {apply_discount(500)}") # uses default discount
    print(f"Price after 80% discount on 1000 (cap test): {apply_discount(1000, 80)}")

"""
Example Output:
Price after 10% discount on 1000: 900.0
Price after default discount on 500: 475.0
Warning: Discount exceeds 60%. Capping at 60%.
Price after 80% discount on 1000 (cap test): 400.0
"""
