championship_stage = input()
ticket_type = input()
tickets_count = int(input())
trophy_photo_option = input()

throphy_photo_price = 40.0
ticket_price = 0.0

if championship_stage == 'Quarter final':
    if ticket_type == 'Standard':
        ticket_price = 55.5
    elif ticket_type == 'Premium':
        ticket_price = 105.2
    elif ticket_type == 'VIP':
        ticket_price = 118.9
elif championship_stage == 'Semi final':
    if ticket_type == 'Standard':
        ticket_price = 75.88
    elif ticket_type == 'Premium':
        ticket_price = 125.22
    elif ticket_type == 'VIP':
        ticket_price = 300.4
elif championship_stage == 'Final':
    if ticket_type == 'Standard':
        ticket_price = 110.1
    elif ticket_type == 'Premium':
        ticket_price = 160.66
    elif ticket_type == 'VIP':
        ticket_price = 400.0

total_price = tickets_count * ticket_price

if total_price > 4000:
    total_price *= 0.75
    throphy_photo_price = 0.0
elif total_price > 2500:
    total_price *= 0.9

if trophy_photo_option == 'Y':
    total_price += tickets_count * throphy_photo_price

print(f'{total_price:.2f}')