fuel_type = input()
fuel_amount = int(input())

if fuel_type == 'Diesel' or fuel_type == 'Gasoline' or fuel_type == 'Gas':
    if fuel_amount >= 25:
        print(f'You have enough {fuel_type.lower()}.')
    elif 0 <= fuel_amount < 25:
        print(f'Fill your tank with {fuel_type.lower()}!')
else:
    print('Invalid fuel!')