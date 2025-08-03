month = input()
number_of_nights = int(input())

price_for_studio = 0.0
price_for_apartment = 0.0
discount_percentage_for_studio = 0
discount_percentage_for_apartment = 0

if month == 'May' or month == 'October':
    price_for_studio = 50.0
    price_for_apartment = 65.0
    if 7 < number_of_nights <= 14:
        discount_percentage_for_studio = 5
    elif number_of_nights > 14:
        discount_percentage_for_studio = 30
elif month == 'June' or month == 'September':
    price_for_studio = 75.2
    price_for_apartment = 68.7
    if number_of_nights > 14:
        discount_percentage_for_studio = 20
elif month == 'July' or month == 'August':
    price_for_studio = 76.0
    price_for_apartment = 77.0

if number_of_nights > 14:
    discount_percentage_for_apartment = 10

total_price_for_studio = (price_for_studio * number_of_nights
                          * (100 - discount_percentage_for_studio) / 100)
total_price_for_apartment = (price_for_apartment * number_of_nights
                             * (100 - discount_percentage_for_apartment) / 100)

print(f'Apartment: {total_price_for_apartment:.2f} lv.')
print(f'Studio: {total_price_for_studio:.2f} lv.')