lily_age = int(input())
wasing_machine_price = float(input())
toy_price = int(input())

money_for_birthday = 10.0
money_increase_for_even_birthday = 10.0
money_for_brother = 1.0

toys_count = 0
total_money_saved = 0.0

for year in range(1, lily_age + 1):
    if year % 2 == 0:
        total_money_saved += money_for_birthday
        total_money_saved -= money_for_brother
        money_for_birthday += money_increase_for_even_birthday
    else:
        toys_count += 1

total_money_saved += toys_count * toy_price

difference = total_money_saved - wasing_machine_price

if difference >= 0:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {abs(difference):.2f}')