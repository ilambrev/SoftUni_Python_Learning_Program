products = {}
input_data = input()

while not input_data == "buy":
    name, price, quantity = input_data.split()

    if name not in products:
        products[name] = {
            "name": name,
            "price": 0,
            "quantity": 0
        }
    products[name]["price"] = float(price)
    products[name]["quantity"] += int(quantity)

    input_data = input()

[print(f"{product['name']} -> {(product['price'] * product['quantity']):.2f}") for product in products.values()]