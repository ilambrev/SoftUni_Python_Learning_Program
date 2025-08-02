spring_rent_size = 3000
summer_autumn_rent_size = 4200
winter_rent_size = 2600

budget = int(input())
season = input()
fishermen_number = int(input())

rent_size = 0
discount_percentage = 0

if fishermen_number <= 6:
    discount_percentage = 10
elif fishermen_number <= 11:
    discount_percentage = 15
elif fishermen_number > 11:
    discount_percentage = 25

if season == 'Spring':
    rent_size = spring_rent_size
elif season == 'Summer' or season == 'Autumn':
    rent_size = summer_autumn_rent_size
elif season == 'Winter':
    rent_size = winter_rent_size

rent_size *= (100 - discount_percentage) / 100 

if fishermen_number % 2 == 0 and season != 'Autumn':
    rent_size *= 1 - 0.05

difference = budget - rent_size

if (difference >= 0):
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {-difference:.2f} leva.')