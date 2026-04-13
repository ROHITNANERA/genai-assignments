"""
Task 3 - Lambda Function: GST Calculator
Create a lambda function gst that returns price after adding 18% GST.
Example:
gst = lambda price: price + (0.18 * price)
print(gst(100)) # should return 118
Extra (optional): Create another lambda to compute final price after GST + discount together.
"""

# Lambda that calculates price after adding 18% GST
gst = lambda price: price + (0.18 * price)

# Extra: Lambda to compute final price after GST + discount (applied sequentially: discount first, then GST)
final_price = lambda price, discount_percent: gst(price - (price * discount_percent / 100))

# Example usage
if __name__ == "__main__":
    # Test GST lambda
    print(f"Price after GST (100): {gst(100)}")  # should return 118
    
    # Test extra lambda (e.g. 100 with 10% discount, then 18% GST)
    print(f"Price after 10% discount and then 18% GST (100): {final_price(100, 10)}")

"""
Example Output:
Price after GST (100): 118.0
Price after 10% discount and then 18% GST (100): 106.2
"""
