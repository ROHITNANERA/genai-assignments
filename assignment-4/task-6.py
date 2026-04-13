"""
Task 6: Read File Safely (Error Handling Inside File Handling Only)
1. Ask the user for a filename to open.
2. If the file exists, read and print it.
3. If it does not exist, print: "File not found. Please check the filename."
Use simple condition checks with os.path.exists() (allowed).
"""

import os

def main():
    filename = input("Enter the filename you want to open: ").strip()

    # Safely check if file exists using os module
    if os.path.exists(filename) and os.path.isfile(filename):
        print(f"\n--- Contents of {filename} ---")
        with open(filename, 'r') as file:
            print(file.read())
    else:
        print("\nFile not found. Please check the filename.")

if __name__ == "__main__":
    main()

"""
Example Output (Simulated Scenario 1 - File Exists):
Enter the filename you want to open: sales_data.txt

--- Contents of sales_data.txt ---
1200
450
980...

Example Output (Simulated Scenario 2 - File Does Not Exist):
Enter the filename you want to open: missing_file.txt

File not found. Please check the filename.
"""
