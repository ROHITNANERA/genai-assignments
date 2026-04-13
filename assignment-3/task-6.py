"""
Task 6 - Combined Utility Function
Write a function process_prices(prices) that:
1. Takes a list of prices.
2. Uses map() + lambda to apply 10% discount to all prices.
3. Uses filter() to keep only discounted prices that are above 300.
4. Returns both lists: discounted_prices, filtered_prices
"""

def process_prices(prices: list[float]) -> tuple[list[float], list[float]]:
    """
    Applies a 10% discount to all prices and filters the ones above 300.
    Returns the fully discounted list, and the filtered list of those 
    discounted prices above 300.
    """
    # Use map() and lambda to apply 10% discount
    discounted_prices = list(map(lambda p: p - (0.10 * p), prices))
    
    # Use filter() and lambda to keep discounted prices > 300
    filtered_prices = list(filter(lambda p: p > 300, discounted_prices))
    
    # Return both list results
    return discounted_prices, filtered_prices

# Test with mock data
if __name__ == "__main__":
    prices_list = [100, 500, 900, 50, 750]
    discounted, filtered = process_prices(prices_list)
    print("--- process_prices results ---")
    print(f"Original prices: {prices_list}")
    print(f"Discounted prices: {discounted}")
    print(f"Filtered prices (above 300): {filtered}")

"""
Example Output:
--- process_prices results ---
Original prices: [100, 500, 900, 50, 750]
Discounted prices: [90.0, 450.0, 810.0, 45.0, 675.0]
Filtered prices (above 300): [450.0, 810.0, 675.0]
"""
