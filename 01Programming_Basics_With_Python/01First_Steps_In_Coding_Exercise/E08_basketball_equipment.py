annual_fee = int(input())

sneakers_price = (1 - 0.4) * annual_fee
basketball_wear_price = (1 - 0.2) * sneakers_price
ball_price = 0.25 * basketball_wear_price
basketball_accessories_price = 0.2 * ball_price

expenses = annual_fee + sneakers_price + basketball_wear_price + \
    ball_price + basketball_accessories_price

print(expenses)