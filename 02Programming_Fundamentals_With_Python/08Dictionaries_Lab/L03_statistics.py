product_data = input()
products = {}

while not product_data == "statistics":
    product, quantity = product_data.split(": ")
    if not products.get(product):
        products[product] = 0
    
    products[product] += int(quantity)

    product_data = input()

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")