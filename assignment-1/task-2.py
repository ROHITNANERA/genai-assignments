# Task 2: Categories (Sets)

# Initial lists to work with
products = ["Laptop", "Smartphone", "Headphones", "Monitor", "Keyboard", "Mouse"]
# 1. Create a short parallel list 'categories' with matching length 
categories = ["Electronics", "Electronics", "Audio", "Electronics", "Accessories", "Accessories"]

# From the list, create a set of categories called 'categories_set'.
categories_set = set(categories)
print("Initial categories set:", categories_set)

# 2. Demonstrate adding a new category to the set and show that duplicates are ignored.
categories_set.add("Networking")
categories_set.add("Electronics")

print("Categories set after adding new and duplicate items:", categories_set)

# 3. Show how to check whether a category exists in the set (print a boolean result).
category_to_check = "Audio"
is_exist_audio = category_to_check in categories_set
print(f"Does '{category_to_check}' exist in categories_set? {is_exist_audio}")

category_to_check = "Furniture"
is_exist_furniture = category_to_check in categories_set
print(f"Does '{category_to_check}' exist in categories_set? {is_exist_furniture}")

# Extra (optional): Show how to get the total number of unique categories using a set.
total_unique_categories = len(categories_set)
print(f"Total number of unique categories: {total_unique_categories}")
