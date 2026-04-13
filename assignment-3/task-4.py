"""
Task 4 - Using map(): Apply GST to List of Prices
Given: prices = [100, 250, 400, 1200, 50]
Use map() with your gst lambda to generate a new list prices_with_gst.
Print both lists: Original prices, Prices after GST
"""

# GST lambda from previous task
gst = lambda price: price + (0.18 * price)

# Given list of prices
prices = [100, 250, 400, 1200, 50]

# Generate a new list applying the GST logic using map()
prices_with_gst = list(map(gst, prices))

# Print both lists for assessment
if __name__ == "__main__":
    print(f"Original prices: {prices}")
    print(f"Prices after GST: {prices_with_gst}")

"""
Example Output:
Original prices: [100, 250, 400, 1200, 50]
Prices after GST: [118.0, 295.0, 472.0, 1416.0, 59.0]
"""
