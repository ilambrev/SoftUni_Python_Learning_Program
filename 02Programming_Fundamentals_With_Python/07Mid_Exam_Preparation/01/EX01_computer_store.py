price_without_taxes = 0.0
taxes = 0.0

input_line = input()

while not input_line == "special" and not input_line == "regular":
    part_price = float(input_line)

    if part_price < 0:
        print("Invalid price!")
    else:
        price_without_taxes += part_price
        taxes += part_price * 0.2

    input_line = input()

total_price = (price_without_taxes + taxes) * 0.9 if input_line == "special" else price_without_taxes + taxes

if total_price == 0:
    print("Invalid order!")
else:
    print(f"""Congratulations you've just bought a new computer!
Price without taxes: {price_without_taxes:.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {total_price:.2f}$""")