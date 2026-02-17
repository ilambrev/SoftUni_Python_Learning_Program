keys_values = input().split()
searched_products = input().split()
products = {}

for i in range(1, len(keys_values), 2):
    products[keys_values[i - 1]] = int(keys_values[i])

for product in searched_products:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")