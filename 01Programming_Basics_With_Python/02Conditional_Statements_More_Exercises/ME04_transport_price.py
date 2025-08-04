distance = int(input())
part_of_day = input()

taxi_initiation_fee = 0.7
taxi_day_fee = 0.79
taxi_night_fee = 0.9
bus_fee = 0.09
bus_min_distance = 20
train_fee = 0.06
train_min_distance = 100

total_price = 0.0

if 1 < distance < 20:
    total_price += taxi_initiation_fee
    if part_of_day == 'day':
        total_price += distance * taxi_day_fee
    elif part_of_day == 'night':
        total_price += distance * taxi_night_fee
elif distance < 100:
    total_price = distance * bus_fee
elif distance >= 100:
    total_price = distance * train_fee

print(f'{total_price:.2f}')