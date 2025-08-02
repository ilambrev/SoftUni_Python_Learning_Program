rose_price = 5.0
dahlia_price = 3.8
tulip_price = 2.8
narcissus_price = 3.0
gladiolus_price = 2.5

flowers_type = input()
flowers_number = int(input())
budget = int(input())

flower_price = 0.0
discount_percentage = 0

if flowers_type == 'Roses':
    flower_price = rose_price
    if flowers_number > 80:
        discount_percentage = 10
elif flowers_type == 'Dahlias':
    flower_price = dahlia_price
    if flowers_number > 90:
        discount_percentage = 15
elif flowers_type == 'Tulips':
    flower_price = tulip_price
    if flowers_number > 80:
        discount_percentage = 15
elif flowers_type == 'Narcissus':
    flower_price = narcissus_price
    if flowers_number < 120:
        discount_percentage = -15
elif flowers_type == 'Gladiolus':
    flower_price = gladiolus_price
    if flowers_number < 80:
        discount_percentage = -20

total_price = flowers_number * flower_price * (100 - discount_percentage) / 100

difference = budget - total_price

if (difference >= 0):
    print(
        f'Hey, you have a great garden with {flowers_number} {flowers_type} and {difference:.2f} leva left.')
else:
    print(f'Not enough money, you need {abs(difference):.2f} leva more.')