budget = float(input())
extras = int(input())
clothing_price_per_extra = float(input())

decor_price = 0.1 * budget

if extras > 150:
    clothing_price_per_extra *= 0.9

total_sum = decor_price + extras * clothing_price_per_extra

if budget - total_sum >= 0:
    print('Action!')
    print(f'Wingard starts filming with {(budget - total_sum):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {(total_sum - budget):.2f} leva more.')