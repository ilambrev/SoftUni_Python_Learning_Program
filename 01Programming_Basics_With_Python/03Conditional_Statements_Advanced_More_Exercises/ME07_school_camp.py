season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

sport = ''
single_price = 0.0

if season == 'Winter':
    if group_type == 'girls':
        single_price = 9.6
        sport = 'Gymnastics'
    elif group_type == 'boys':
        single_price = 9.6
        sport = 'Judo'
    elif group_type == 'mixed':
        single_price = 10.0
        sport = 'Ski'
elif season == 'Spring':
    if group_type == 'girls':
        single_price = 7.2
        sport = 'Athletics'
    elif group_type == 'boys':
        single_price = 7.2
        sport = 'Tennis'
    elif group_type == 'mixed':
        single_price = 9.5
        sport = 'Cycling'
elif season == 'Summer':
    if group_type == 'girls':
        single_price = 15.0
        sport = 'Volleyball'
    elif group_type == 'boys':
        single_price = 15.0
        sport = 'Football'
    elif group_type == 'mixed':
        single_price = 20.0
        sport = 'Swimming'

discount_percentage = 0

if 10 <= students_count < 20:
    discount_percentage = 5
elif 20 <= students_count < 50:
    discount_percentage = 15
elif students_count >= 50:
    discount_percentage = 50

total_price = (students_count
               * nights_count
               * single_price
               * (100 - discount_percentage) / 100)

print(f'{sport} {total_price:.2f} lv.')