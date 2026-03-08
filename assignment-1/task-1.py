# Task 1: Product Collections (Lists & Tuples)

# 1. Create a list named 'products' containing at least 6 product names (strings).
products = ["Laptop", "Smartphone", "Headphones", "Monitor", "Keyboard", "Mouse"]

# 2. Create a tuple named 'sample_product' that stores (product_name, price, category) for one product.
sample_product = ("Laptop", 999.99, "Electronics")

# 3. Print the 2nd and last product from the products list.
print("2nd product:", products[1])
print("Last product:", products[-1])

products.append("Tablet")
products.append("Smartwatch")
print("Updated products list:", products)

sample_product_list = list(sample_product)
sample_product_list[1] = 1049.99
sample_product = tuple(sample_product_list)

print("Updated sample_product tuple:", sample_product)
