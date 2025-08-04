from math import floor, ceil

days = int(input())
foot_available_in_kg = int(input())
dog_food_per_day_in_kg = float(input())
cat_food_per_day_in_kg = float(input())
turtle_food_per_day_in_gr = float(input())

food_needed = days * (dog_food_per_day_in_kg
                      + cat_food_per_day_in_kg
                      + turtle_food_per_day_in_gr / 1000)

difference = foot_available_in_kg - food_needed

if (difference >= 0):
    print(f'{floor(difference)} kilos of food left.')
else:
    print(f'{ceil(abs(difference))} more kilos of food are needed.')