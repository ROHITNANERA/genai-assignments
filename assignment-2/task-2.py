# Task 2: Process Multiple Orders
orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_count = 0

# Processing all fixed orders sequentially. Building on the discount logic 
# from task 1 but adapted for a batch scenario.
for order in orders:
    if order >= 2000:
        discount_pct = 15
    elif order >= 1500:
        discount_pct = 10
    elif order >= 1000:
        discount_pct = 7
    else:
        discount_pct = 0
        
    final_amount = order - (order * discount_pct / 100)
    total_revenue += final_amount
    
    # Optional Extra: Count orders that received a reduction
    if discount_pct > 0:
        discounted_count += 1
        
    print(f"{order} -> {discount_pct}% -> {final_amount}")

print(f"\nTotal Revenue: {total_revenue}")
print(f"Orders with discounts applied: {discounted_count}")

'''
Example Output:
1200 -> 7% -> 1116.0
2500 -> 15% -> 2125.0
800 -> 0% -> 800.0
1750 -> 10% -> 1575.0
3000 -> 15% -> 2550.0

Total Revenue: 8166.0
Orders with discounts applied: 4
'''
