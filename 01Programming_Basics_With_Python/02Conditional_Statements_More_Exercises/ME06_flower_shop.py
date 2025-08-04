from math import floor, ceil

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cacti_count = int(input())
gift_price = float(input())

magnolia_price = 3.25
hyacinth_price = 4.0
rose_price = 3.5
cactus_price = 8.0
tax_percentage = 5

order_amount = (magnolias_count * magnolia_price
                + hyacinths_count * hyacinth_price
                + roses_count * rose_price
                + cacti_count * cactus_price)

final_income = order_amount * (100 - tax_percentage) / 100

difference = final_income - gift_price

if (difference >= 0):
    print(f'She is left with {floor(difference)} leva.')
else:
    print(f'She will have to borrow {ceil(abs(difference))} leva.')