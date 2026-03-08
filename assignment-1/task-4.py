# Task 4: Combined Operations

# Initial datasets based on previous tasks
products = ["Laptop", "Smartphone", "Headphones", "Monitor", "Keyboard", "Mouse"]
categories = ["Electronics", "Electronics", "Audio", "Electronics", "Accessories", "Accessories"]
price_dict = {
    "Laptop": 999.99,
    "Smartphone": 699.99,
    "Headphones": 149.99,
    "Monitor": 299.99,
    "Keyboard": 49.99,
    "Mouse": 29.99
}

# 1. Using the products list and price_dict, create a list of tuples named 'catalog'
# where each tuple is (product_name, price, category).
catalog = []
for i in range(len(products)):
    product_name = products[i]
    category = categories[i]
    # Fetch price from price_dict using .get() to handle any potential missing keys gracefully
    price = price_dict.get(product_name, 0.0)
    
    # Create the tuple and add it to the catalog list
    item_tuple = (product_name, price, category)
    catalog.append(item_tuple)

print("Catalog list of tuples:")
for item in catalog:
    print(" ", item)

# 2. From 'catalog', create a new dictionary 'category_to_products' that maps each category 
# to a list of product names in that category.
category_to_products = {}
for product_name, price, category in catalog:
    # If the category is not yet a key in the dictionary, initialize it with an empty list
    if category not in category_to_products:
        category_to_products[category] = []
        
    # Append the product to the appropriate category list
    category_to_products[category].append(product_name)

print("\nCategory to products mapping:")
for cat, prod_list in category_to_products.items():
    print(f" {cat}: {prod_list}")

# 3. Print all products that belong to the category that has the maximum number of Products.
max_products_category = None
max_products_count = 0

# Find the category with maximum products
for category, prod_list in category_to_products.items():
    current_count = len(prod_list)
    if current_count > max_products_count:
        max_products_count = current_count
        max_products_category = category

# Output the result if a category was found
if max_products_category:
    print(f"\nCategory with maximum products: '{max_products_category}' (Count: {max_products_count})")
    print(f"Products in this category: {category_to_products[max_products_category]}")
