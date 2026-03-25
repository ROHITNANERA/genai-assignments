# Task 3: User Menu
orders = []

# Core event loop using while True. The loop only terminates via the explicitly defined 'q' condition.
while True:
    print("\n--- Menu ---")
    print("1 - Add order amount")
    print("2 - Show all orders and totals")
    print("q - Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        raw_amt = input("Enter order amount to add: ")
        if raw_amt.isdigit():
            orders.append(int(raw_amt))
        else:
            print("Invalid input, expected an integer amount.")
            
    elif choice == '2':
        # Re-applying same discount tiers dynamically. 
        # (Usually I'd abstract this into a function, but sticking to loop/condition constraint)
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
            print(f"Order: {order} | Discount: {discount_pct}% | Final: {final_amount}")
            
    elif choice == 'q':
        print("Exiting the menu.")
        break
        
    else:
        # Invalid selection: show an error and restart the loop immediately
        print("Unrecognized menu option. Please try again.")
        continue

'''
Example Output:
--- Menu ---
1 - Add order amount
2 - Show all orders and totals
q - Quit
Enter your choice: 1
Enter order amount to add: 1100

--- Menu ---
1 - Add order amount
2 - Show all orders and totals
q - Quit
Enter your choice: 2
Order: 1100 | Discount: 7% | Final: 1023.0

--- Menu ---
1 - Add order amount
2 - Show all orders and totals
q - Quit
Enter your choice: q
Exiting the menu.
'''
