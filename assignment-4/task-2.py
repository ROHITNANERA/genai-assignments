"""
Task 2: Read File in Different Ways
Using the same sales_data.txt:
1. Read the entire file using .read() and print it.
2. Read the first line using .readline().
3. Read all lines using .readlines() and convert them into a list of integers.
"""

def main():
    filename = "sales_data.txt"
    
    print("--- 1. Using .read() ---")
    with open(filename, 'r') as file:
        print(file.read())

    print("--- 2. Using .readline() ---")
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
        print(f"First line: {first_line}")

    print("\n--- 3. Using .readlines() to list of ints ---")
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        # I am using a simple for-loop to convert each line to a number
        # I learned this loop pattern in the previous control flow assignment
        sales_integers = []
        for line in lines:
            line = line.strip()
            # converting the text to integer without complex checks
            sales_integers.append(int(line))
            
        print(f"List of integers: {sales_integers}")

if __name__ == "__main__":
    main()

"""
Example Output:
--- 1. Using .read() ---
1200
450
980
1500
3000

--- 2. Using .readline() ---
First line: 1200

--- 3. Using .readlines() to list of ints ---
List of integers: [1200, 450, 980, 1500, 3000]
"""
