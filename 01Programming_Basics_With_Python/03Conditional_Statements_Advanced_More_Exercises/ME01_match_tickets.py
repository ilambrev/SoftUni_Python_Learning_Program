budget = float(input())
ticket_cathegory = input()
people_count = int(input())

vip_ticket_price = 499.99
normal_ticket_price = 249.99

transport_cost_percentage = 0

if 1 <= people_count <= 4:
    transport_cost_percentage = 75
elif 5 <= people_count <= 9:
    transport_cost_percentage = 60
elif 10 <= people_count <= 24:
    transport_cost_percentage = 50
elif 25 <= people_count <= 49:
    transport_cost_percentage = 40
elif people_count >= 50:
    transport_cost_percentage = 25

expenses = budget * transport_cost_percentage / 100

ticket_price = 0.0

if ticket_cathegory == 'VIP':
    ticket_price = vip_ticket_price
elif ticket_cathegory == 'Normal':
    ticket_price = normal_ticket_price

expenses += people_count * ticket_price

difference = budget - expenses

if difference >= 0:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(difference):.2f} leva.')