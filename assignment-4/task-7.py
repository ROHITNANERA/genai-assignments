"""
Task 7: Mini Project - Export Discounted Prices
Dictionary `prices = { "Mouse": 500, "Keyboard": 800, "Monitor": 7000, "Pendrive": 400, "Camera": 5000 }`
Ask user for discount percentage.
Write discounted prices to `discount_report.txt` using `Product | Original Price | Discounted Price`.
After writing, read and print.
Extra: Summary at bottom of file:
Total Items: X
Average Discounted Price: Y
"""

def main():
    prices = {
        "Mouse": 500,
        "Keyboard": 800,
        "Monitor": 7000,
        "Pendrive": 400,
        "Camera": 5000
    }
    
    filename = "discount_report.txt"

    # Ask user for discount percentage
    # Ask user for discount percentage
    # I am assuming the user enters a valid number, keeping it simple as I learned recently
    discount_input = input("Enter discount percentage (e.g. 10 for 10%): ")
    discount_percent = float(discount_input)

    total_discounted_sum = 0
    item_count = len(prices)

    # Write logic
    with open(filename, 'w') as file:
        file.write("Product | Original Price | Discounted Price\n")
        file.write("-" * 45 + "\n")
        
        for product, original_price in prices.items():
            # Calculate discount
            discounted_price = original_price - (original_price * discount_percent / 100)
            total_discounted_sum += discounted_price
            
            # Writing using simple f-strings without advanced formatting
            file.write(f"{product} | {original_price} | {discounted_price}\n")
        
        # Write summary
        file.write("-" * 45 + "\n")
        file.write(f"Total Items: {item_count}\n")
        if item_count > 0:
            avg_discount = total_discounted_sum / item_count
            file.write(f"Average Discounted Price: {avg_discount:.2f}\n")

    # Read and print logic
    print(f"\n--- Generated {filename} Content ---\n")
    with open(filename, 'r') as file:
        print(file.read())

if __name__ == "__main__":
    main()

"""
Example Output (Simulated):
Enter discount percentage (e.g. 10 for 10%): 20

--- Generated discount_report.txt Content ---

Product | Original Price | Discounted Price
---------------------------------------------
Mouse      | 500            | 400.00
Keyboard   | 800            | 640.00
Monitor    | 7000           | 5600.00
Pendrive   | 400            | 320.00
Camera     | 5000           | 4000.00
---------------------------------------------
Total Items: 5
Average Discounted Price: 2192.00

"""
