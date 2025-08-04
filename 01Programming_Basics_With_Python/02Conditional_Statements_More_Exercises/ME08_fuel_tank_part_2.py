fuel_type = input()
fuel_amount = float(input())
is_club_card_available = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

gasoline_discount = 0.18
diesel_discount = 0.12
gas_discount = 0.08
first_level_quantity_discount_percentage = 8
second_level_quantity_discount_percentage = 10

fuel_price = 0

if fuel_type == 'Gasoline':
    fuel_price = gasoline_price
    if is_club_card_available == 'Yes':
        fuel_price -= gasoline_discount
elif fuel_type == 'Diesel':
    fuel_price = diesel_price
    if is_club_card_available == 'Yes':
        fuel_price -= diesel_discount
elif fuel_type == 'Gas':
    fuel_price = gas_price
    if is_club_card_available == 'Yes':
        fuel_price -= gas_discount

total_price = fuel_amount * fuel_price

if 20 <= fuel_amount <= 25:
    total_price *= (100 - first_level_quantity_discount_percentage) / 100
elif fuel_amount > 25:
    total_price *= (100 - second_level_quantity_discount_percentage) / 100

print(f'{total_price:.2f} lv.')