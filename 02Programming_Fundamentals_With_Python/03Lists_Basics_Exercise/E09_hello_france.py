items = input().split("|")
budget = float(input())

train_ticket_price = 150.0
markup_percentage = 40
bought_items_prices = []
profit = 0

for item in items:
    item_type, price = item.split("->")
    price = float(price)

    is_price_acceptable = False

    if item_type == "Clothes" and price <= 50.00:
        is_price_acceptable = True
    elif item_type == "Shoes" and price <= 35.00:
        is_price_acceptable = True
    elif item_type == "Accessories" and price <= 20.50:
        is_price_acceptable = True

    if is_price_acceptable and price <= budget:
        budget -= price
        new_price = price * (100 + markup_percentage) / 100
        profit += new_price - price
        bought_items_prices.append(new_price)

total_sum = sum(bought_items_prices) + budget

print(f"{' '.join([f'{price:.2f}' for price in bought_items_prices])}")
print(f"Profit: {profit:.2f}")

if total_sum >= train_ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")