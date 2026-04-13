"""
Task 1: Write Sales Records to a File
1. Create a list of sales amounts: sales = [1200, 450, 980, 1500, 3000]
2. Open a file named sales_data.txt in write mode.
3. Write each sale on a new line in the file.
4. Close the file, then reopen it and print its contents.
"""

def main():
    sales = [1200, 450, 980, 1500, 3000]
    filename = "sales_data.txt"

    # Write sales to file
    with open(filename, 'w') as file:
        for sale in sales:
            file.write(f"{sale}\n")

    # Reopen and print contents
    print("--- File Contents ---")
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

if __name__ == "__main__":
    main()

"""
Example Output:
--- File Contents ---
1200
450
980
1500
3000

"""
