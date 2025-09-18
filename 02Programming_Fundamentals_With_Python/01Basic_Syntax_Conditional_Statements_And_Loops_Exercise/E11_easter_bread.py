budget = float(input())
flour_price_per_kg = float(input())

eggs_price_per_pack = 0.75 * flour_price_per_kg
milk_price_per_liter = 1.25 * flour_price_per_kg

loaves_counter = 0
eggs_counter = 0

while budget > 0:
    products_price = (eggs_price_per_pack
                      + flour_price_per_kg
                      + milk_price_per_liter / 4)

    if products_price <= budget:
        budget -= products_price
        loaves_counter += 1
        eggs_counter += 3

        if loaves_counter % 3 == 0:
            eggs_counter -= loaves_counter - 2

    else:
        break

print(f'You made {loaves_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.')