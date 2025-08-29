from math import floor, ceil

tennis_racket_price = float(input())
tennis_rackets_count = int(input())
sneakers_pairs_count = int(input())

sneakers_pair_price = tennis_racket_price / 6

total_rackets_price = tennis_rackets_count * tennis_racket_price
total_sneakers_pairs_price = sneakers_pairs_count * sneakers_pair_price
total_other_equipment_price = (total_rackets_price + total_sneakers_pairs_price) * 0.2

total_price = (total_rackets_price
               + total_sneakers_pairs_price
               + total_other_equipment_price)

price_paid_by_djokovic = total_price / 8
price_paid_by_sponsors = total_price - price_paid_by_djokovic

print(f'Price to be paid by Djokovic {floor(price_paid_by_djokovic)}')
print(f'Price to be paid by sponsors {ceil(price_paid_by_sponsors)}')