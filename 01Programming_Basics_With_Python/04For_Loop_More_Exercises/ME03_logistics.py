loads_number = int(input())

van_price_per_ton = 200
truck_price_per_ton = 175
train_price_per_ton = 120

total_van_load = 0
total_truck_load = 0
total_train_load = 0

for _ in range(loads_number):
    current_load_in_tons = int(input())

    if current_load_in_tons <= 3:
        total_van_load += current_load_in_tons
    elif current_load_in_tons <= 11:
        total_truck_load += current_load_in_tons
    else:
        total_train_load += current_load_in_tons

total_price = (total_van_load * van_price_per_ton
               + total_truck_load * truck_price_per_ton
               + total_train_load * train_price_per_ton)

total_load = total_van_load + total_truck_load + total_train_load

average_price_per_ton = total_price / total_load
van_load_percentage = 100 * total_van_load / total_load
truck_load_percentage = 100 * total_truck_load / total_load
train_load_percentage = 100 * total_train_load / total_load

print(f'{average_price_per_ton:.2f}')
print(f'{van_load_percentage:.2f}%')
print(f'{truck_load_percentage:.2f}%')
print(f'{train_load_percentage:.2f}%')