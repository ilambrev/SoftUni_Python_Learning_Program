mackerel_price = float(input())
sprat_price = float(input())
bonito_amount = float(input())
horse_mackerel_amount = float(input())
mussels_amount = float(input())

bonito_price = mackerel_price * 1.6
horse_mackerel_price = sprat_price * 1.8
mussels_price = 7.5

total_price = (bonito_amount * bonito_price
               + horse_mackerel_amount * horse_mackerel_price
               + mussels_amount * mussels_price)

print(f'{total_price:.2f}')