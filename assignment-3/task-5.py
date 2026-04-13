"""
Task 5 - Using filter(): Filter Expensive Products
Given the list: prices = [100, 250, 400, 1200, 50, 2000, 850]
Use filter() to:
1. Create a list of prices greater than 500.
2. Create another list of prices less than or equal to 500.
Print both lists.
"""

# Given list of prices
prices = [100, 250, 400, 1200, 50, 2000, 850]

# Filter condition 1: List of prices greater than 500
expensive_products = list(filter(lambda x: x > 500, prices))

# Filter condition 2: List of prices less than or equal to 500
budget_products = list(filter(lambda x: x <= 500, prices))

# Print both lists
if __name__ == "__main__":
    print(f"Prices greater than 500: {expensive_products}")
    print(f"Prices less than or equal to 500: {budget_products}")

"""
Example Output:
Prices greater than 500: [1200, 2000, 850]
Prices less than or equal to 500: [100, 250, 400, 50]
"""
