days_to_stay = int(input())
type_of_room = input()
rate = input()

overnight_stay_price = 0.0
discount_percentage = 0

overnigt_stay_count = days_to_stay - 1

if type_of_room == 'room for one person':
    overnight_stay_price = 18.0
elif type_of_room == 'apartment':
    overnight_stay_price = 25.0
    if 1 < days_to_stay < 10:
        discount_percentage = 30
    elif 10 <= days_to_stay <= 15:
        discount_percentage = 35
    elif days_to_stay > 15:
        discount_percentage = 50
elif type_of_room == 'president apartment':
    overnight_stay_price = 35.0
    if 1 < days_to_stay < 10:
        discount_percentage = 10
    elif 10 <= days_to_stay <= 15:
        discount_percentage = 15
    elif days_to_stay > 15:
        discount_percentage = 20

total_price = overnigt_stay_count * \
    overnight_stay_price * (100 - discount_percentage) / 100

if rate == 'positive':
    total_price *= (100 + 25) / 100
elif rate == 'negative':
    total_price *= (100 - 10) / 100

print(f'{total_price:.2f}')