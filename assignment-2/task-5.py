# Task 5: Loop Control with Conditions
daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

# Iterating the data stream to demonstrate mid-loop control flows
for sales in daily:
    if sales == -1:
        # Corrupted flag encountered, terminating early to avoid bad data
        print("Encountered corrupted data (-1). Halting processing immediately.")
        break
        
    elif sales == 0:
        # Day with no sales, bypassing the accumulation steps
        continue
        
    total_sales += sales
    print(f"Processed valid sale: {sales} | Running total: {total_sales}")

print(f"\nFinal total sales accumulated: {total_sales}")

'''
Example Output:
Processed valid sale: 200 | Running total: 200
Processed valid sale: 150 | Running total: 350
Processed valid sale: 400 | Running total: 750
Processed valid sale: 50 | Running total: 800
Encountered corrupted data (-1). Halting processing immediately.

Final total sales accumulated: 800
'''
