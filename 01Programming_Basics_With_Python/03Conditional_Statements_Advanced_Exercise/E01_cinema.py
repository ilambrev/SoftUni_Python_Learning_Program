projection_type = input()
sits_rows = int(input())
sits_cols = int(input())

ticket_price = 0

total_cinema_sits = sits_rows * sits_cols

if projection_type == 'Premiere':
    ticket_price = 12.00
elif projection_type == 'Normal':
    ticket_price = 7.50
elif projection_type == 'Discount':
    ticket_price = 5.00

total_incomes = total_cinema_sits * ticket_price

print(f'{total_incomes:.2f} leva')