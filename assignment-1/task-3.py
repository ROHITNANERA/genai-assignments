# Task 3: Product Pricing (Dictionaries)

price_dict = {
    "Laptop": 999,
    "Smartphone": 699,
    "Headphones": 149,
    "Monitor": 299,
    "Keyboard": 49,
    "Mouse": 29
}

price_dict["Tablet"] = 399
print("Dictionary after adding a new product:\n", price_dict)

price_dict["Smartphone"] = 649
print("Dictionary after updating the price of Smartphone:\n", price_dict)

product_to_remove = "Monitor"
if product_to_remove in price_dict:
    del price_dict[product_to_remove]
    print(f"Successfully removed '{product_to_remove}'.")
else:
    print(f"Product '{product_to_remove}' not found in dictionary.")

non_existent_product = "UnknownProduct"
if non_existent_product in price_dict:
    del price_dict[non_existent_product]
else:
    print(f"Product '{non_existent_product}' not found, nothing to remove.")

if len(price_dict) > 0:
    total_price = sum(price_dict.values())
    average_price = total_price / len(price_dict)
    print(f"Average price of all products: ${average_price}")
else:
    print("Cannot calculate average price because the dictionary is empty.")

if price_dict:
    max_price_product = max(price_dict, key=price_dict.get)
    min_price_product = min(price_dict, key=price_dict.get)
    
    print(f"Product with maximum price: {max_price_product} (${price_dict[max_price_product]})")
    print(f"Product with minimum price: {min_price_product} (${price_dict[min_price_product]})")
