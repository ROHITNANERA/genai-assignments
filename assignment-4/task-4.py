"""
Task 4: Generate Summary Report from File
Using only file reading operations:
1. Read all sales values from sales_data.txt.
2. Convert them into integers.
3. Calculate and print: Total Sales, Highest Sale, Lowest Sale, Average Sale
"""

def main():
    filename = "sales_data.txt"
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        sales = [int(line.strip()) for line in lines if line.strip().isdigit()]

    if not sales:
        print("No sales data available.")
        return

    total_sales = sum(sales)
    highest_sale = max(sales)
    lowest_sale = min(sales)
    average_sale = total_sales / len(sales)

    print("--- Sales Summary Report ---")
    print(f"Total Sales: {total_sales}")
    print(f"Highest Sale: {highest_sale}")
    print(f"Lowest Sale: {lowest_sale}")
    print(f"Average Sale: {average_sale:.2f}")

if __name__ == "__main__":
    main()

"""
Example Output:
--- Sales Summary Report ---
Total Sales: 16330
Highest Sale: 5000
Lowest Sale: 450
Average Sale: 2041.25
"""
