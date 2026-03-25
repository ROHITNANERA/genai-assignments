# Task 1: Discount Rules

# Note: Keeping the non-numeric check simple without try/except since 
# we are focusing only on conditionals right now.
raw_input = input("Enter order amount: ")

if not raw_input.isdigit():
    print("Error: Input is not a valid numeric amount.")
    exit()

order_amount = int(raw_input)

# Applying tiered discount structure. Top-down approach works best here 
# to catch the highest applicable discount automatically.
if order_amount >= 2000:
    discount_pct = 15
elif order_amount >= 1500:
    discount_pct = 10
elif order_amount >= 1000:
    discount_pct = 7
else:
    discount_pct = 0

discount_amt = order_amount * (discount_pct / 100)
subtotal = order_amount - discount_amt

# Optional Extra requirement: 5% flat tax calculation
tax = subtotal * 0.05
final_total = subtotal + tax

print(f"Subtotal: {subtotal}")
print(f"Tax: {tax}")
print(f"Final Total: {final_total}")

'''
Example Output:
Enter order amount: 2500
Subtotal: 2125.0
Tax: 106.25
Final Total: 2231.25
'''
