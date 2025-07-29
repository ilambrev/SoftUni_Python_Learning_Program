budget = float(input())
gpu_amoutn = int(input())
cpu_amount = int(input())
ram_amount = int(input())

gpu_price = 250
gpu_total_price = gpu_amoutn * gpu_price
cpu_price = gpu_total_price * 0.35
cpu_total_price = cpu_amount * cpu_price
ram_price = gpu_total_price * 0.1
ram_total_price = ram_amount * ram_price

total_price = (gpu_total_price
               + cpu_total_price
               + ram_total_price)

if gpu_amoutn > cpu_amount:
    total_price *= 0.85

difference = budget - total_price

if (difference >= 0):
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {abs(difference):.2f} leva more!')