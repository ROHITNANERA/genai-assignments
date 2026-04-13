"""
Task 5: Create Product Info File (User Input)
1. Ask the user for 3 product names & their prices.
2. Write them into a new file products.txt in this format: ProductName | Price
3. Read the file and print each line with proper formatting.
"""

def main():
    filename = "products.txt"
    num_products = 3
    
    # Collect data from user and write to file
    with open(filename, 'w') as file:
        print(f"Enter details for {num_products} products:")
        for i in range(num_products):
            # Prompt for name and price
            name = input(f"Product {i+1} Name: ").strip()
            price = input(f"Product {i+1} Price: ").strip()
            # Write structured format
            file.write(f"{name} | {price}\n")
            
    print("\n--- Data Saved to File ---\n")

    # Read and print from file
    print("--- Products in File ---")
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 2:
                print(f"Item: {parts[0].strip():<15} Cost: ${parts[1].strip()}")
            else:
                print(line.strip())

if __name__ == "__main__":
    main()

"""
Example Output (Simulated):
Enter details for 3 products:
Product 1 Name: Apple
Product 1 Price: 1.50
Product 2 Name: Banana
Product 2 Price: 0.80
Product 3 Name: Orange
Product 3 Price: 1.20

--- Data Saved to File ---

--- Products in File ---
Item: Apple           Cost: $1.50
Item: Banana          Cost: $0.80
Item: Orange          Cost: $1.20
"""
