"""
Task 3: Append New Sales
1. Append these new sales to the same file: 5000, 2500, 1700
2. After appending, reopen and print the entire updated file.
Extra (optional): Print the total number of lines after appending.
"""

def main():
    filename = "sales_data.txt"
    new_sales = [5000, 2500, 1700]

    # Append new sales
    with open(filename, 'a') as file:
        for sale in new_sales:
            file.write(f"{sale}\n")

    # Reopen, print content, and count lines
    print("--- Updated File Contents ---")
    line_count = 0
    with open(filename, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        for line in lines:
            print(line.strip())

    print(f"\nTotal number of lines: {line_count}")

if __name__ == "__main__":
    main()

"""
Example Output:
--- Updated File Contents ---
1200
450
980
1500
3000
5000
2500
1700

Total number of lines: 8
"""
