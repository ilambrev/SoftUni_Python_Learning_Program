hour = int(input())
day = input()
shop_status = ''

if hour < 10 or hour > 18 or day == 'Sunday':
    shop_status = 'closed'
else:
    shop_status = 'open'

print(shop_status)