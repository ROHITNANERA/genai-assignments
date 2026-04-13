"""
Task 7 - Mini Problem: Menu Using Functions
Create the following three small functions:
1. add_price(prices_list, price) -> adds price to the list.
2. get_average_price(prices_list) -> returns average price.
3. get_max_price(prices_list) -> returns the maximum price.
Then create a simple menu:
1 -> Add price
2 -> Show average price
3 -> Show highest price
q -> Quit
Use only loops + function calls (no OOP).
"""

def add_price(prices_list: list[float], price: float) -> None:
    """Adds a valid numeric price to the prices list."""
    prices_list.append(price)

def get_average_price(prices_list: list[float]) -> float:
    """Calculates and returns the average price. Avoids division by zero."""
    if not prices_list:
        return 0.0
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list: list[float]) -> float:
    """Returns the highest price from the prices list."""
    if not prices_list:
        return 0.0
    return max(prices_list)

def main():
    """Main menu loop for interacting with the utility functions."""
    prices = []
    
    while True:
        print("\n--- Price Menu ---")
        print("1 -> Add price")
        print("2 -> Show average price")
        print("3 -> Show highest price")
        print("q -> Quit")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == '1':
            try:
                new_price = float(input("Enter price to add: "))
                if new_price < 0:
                    print("Price cannot be negative.")
                else:
                    add_price(prices, new_price)
                    print(f"Price {new_price} added successfully!")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
        elif choice == '2':
            average = get_average_price(prices)
            print(f"Average price: {average:.2f}")
            
        elif choice == '3':
            maximum = get_max_price(prices)
            print(f"Highest price: {maximum:.2f}")
            
        elif choice == 'q':
            print("Exiting application...")
            break
            
        else:
            print("Invalid choice. Please select from the menu.")

# Entry point of the script
if __name__ == "__main__":
    main()

"""
Example Output (Simulated):

--- Price Menu ---
1 -> Add price
2 -> Show average price
3 -> Show highest price
q -> Quit
Enter your choice: 1
Enter price to add: 100
Price 100.0 added successfully!

--- Price Menu ---
1 -> Add price
2 -> Show average price
3 -> Show highest price
q -> Quit
Enter your choice: 2
Average price: 100.00

--- Price Menu ---
1 -> Add price
2 -> Show average price
3 -> Show highest price
q -> Quit
Enter your choice: q
Exiting application...
"""
