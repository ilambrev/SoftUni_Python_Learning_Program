season = input()
kilometers_monthly = float(input())

tax_percentage = 10
price_per_kilometer = 0.0

if kilometers_monthly <= 5000:
    if season == 'Spring' or season == 'Autumn':
        price_per_kilometer = 0.75
    elif season == 'Summer':
        price_per_kilometer = 0.9
    elif season == 'Winter':
        price_per_kilometer = 1.05
elif kilometers_monthly <= 10000:
    if season == 'Spring' or season == 'Autumn':
        price_per_kilometer = 0.95
    elif season == 'Summer':
        price_per_kilometer = 1.1
    elif season == 'Winter':
        price_per_kilometer = 1.25
elif kilometers_monthly <= 20000:
    price_per_kilometer = 1.45

salary = 4 * kilometers_monthly * price_per_kilometer
salary *= (100 - tax_percentage) / 100

print(f'{salary:.2f}')