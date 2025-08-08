budget = float(input())
season = input()

location = ''
accommodation = ''
price = 0.0

if season == 'Summer':
    location = 'Alaska'
elif season == 'Winter':
    location = 'Morocco'

if budget <= 1000:
    accommodation = 'Camp'
    if season == 'Summer':
        price = budget * 0.65
    elif season == 'Winter':
        price = budget * 0.45
elif budget <= 3000:
    accommodation = 'Hut'
    if season == 'Summer':
        price = budget * 0.8
    elif season == 'Winter':
        price = budget * 0.6
elif budget > 3000:
    accommodation = 'Hotel'
    price = budget * 0.9

print(f'{location} - {accommodation} - {price:.2f}')