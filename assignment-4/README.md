# Assignment 4: File Handling (Read, Write, Append, Modes)

This assignment focuses on opening, reading, appending, and interacting with files using Python's native `open()` protocols and associated context blocks (`with open()`).

## Contents
* **`task-1.py`**: Write Sales Records to a File (`sales_data.txt`)
* **`task-2.py`**: Read File in Different Ways (modes: `read()`, `readline()`, `readlines()`)
* **`task-3.py`**: Append New Sales
* **`task-4.py`**: Generate Data/Summary Report from existing File content
* **`task-5.py`**: Create Product Info File based on User Input (`products.txt`)
* **`task-6.py`**: Defensive file reading securely checking against `os.path.exists()` before interactions
* **`task-7.py`**: Interactive Mini-Project outputting a formatted export sheet (`discount_report.txt`)

## How to execute
Executing these tasks may create or modify side-files inside this directory such as `sales_data.txt`, `products.txt` and `discount_report.txt`.

Ensure to run locally from this directly so the file creation scope exists within your project tree:
```bash
python task-1.py
```

## Reflection
* **What I learned:** I learned how to use Python's `open()` function with different modes like read (`r`), write (`w`), and append (`a`). Using the `with` statement was also a new concept that helps manage files safely so I don't forget to close them.
* **What was challenging:** Understanding the differences between `.read()`, `.readline()`, and `.readlines()` took some experimenting. Also, making sure I convert the text read from a file into integers before doing math on it was a common mistake I had to fix. Getting comfortable with basic loops instead of advanced list comprehensions helped me understand string parsing better. 
* **What I'd do differently:** In the future, I will start with simple code that solves the problem directly before trying to format things perfectly or using advanced checks like `try-except` blocks preemptively. Sticking to the basic tools I've practiced more recently builds a stronger foundation!
