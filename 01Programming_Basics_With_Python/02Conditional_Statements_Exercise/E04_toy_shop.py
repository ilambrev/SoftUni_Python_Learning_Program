puzzle_price = 2.6
talking_doll_price = 3
teddy_bear_price = 4.1
minion_price = 8.2
truck_price = 2
number_of_toys_for_discount = 50
discount_percentage = 25
rent_percentage = 10

trip_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

profit = (puzzles * puzzle_price
          + talking_dolls * talking_doll_price
          + teddy_bears * teddy_bear_price
          + minions * minion_price
          + trucks * truck_price)

number_of_toys = puzzles + talking_dolls + teddy_bears + minions + trucks

if number_of_toys >= number_of_toys_for_discount:
    profit = profit * (100 - discount_percentage) / 100

profit = profit * (100 - rent_percentage) / 100

if profit >= trip_price:
    print(f'Yes! {(profit - trip_price):.2f} lv left.')
else:
    print(f'Not enough money! {(trip_price - profit):.2f} lv needed.')