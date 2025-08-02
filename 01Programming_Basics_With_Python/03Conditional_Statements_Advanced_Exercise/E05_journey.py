budget = float(input())
season = input()

destination = ''
accommodation_type = ''
expenses = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        accommodation_type = 'Camp'
        expenses = budget * 0.3
    elif season == 'winter':
        accommodation_type = 'Hotel'
        expenses = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        accommodation_type = 'Camp'
        expenses = budget * 0.4
    elif season == 'winter':
        accommodation_type = 'Hotel'
        expenses = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    accommodation_type = 'Hotel'
    expenses = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{accommodation_type} - {expenses:.2f}')