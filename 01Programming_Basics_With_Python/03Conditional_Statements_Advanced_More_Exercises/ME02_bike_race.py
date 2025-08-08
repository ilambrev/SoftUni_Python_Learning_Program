juniors_count = int(input())
seniors_count = int(input())
track_type = input()

organizational_costs_percentage = 5
fee_dicount_percentage = 25

junior_fee = 0.0
senior_fee = 0.0

if track_type == 'trail':
    junior_fee = 5.5
    senior_fee = 7.0
elif track_type == 'cross-country':
    junior_fee = 8.0
    senior_fee = 9.5
    participants = juniors_count + seniors_count
    if participants >= 50:
        junior_fee *= (100 - fee_dicount_percentage) / 100
        senior_fee *= (100 - fee_dicount_percentage) / 100
elif track_type == 'downhill':
    junior_fee = 12.25
    senior_fee = 13.75
elif track_type == 'road':
    junior_fee = 20.0
    senior_fee = 21.50

donation_amount = (juniors_count * junior_fee
                   + seniors_count * senior_fee)

donation_amount *= (100 - organizational_costs_percentage) / 100

print(f'{donation_amount:.2f}')