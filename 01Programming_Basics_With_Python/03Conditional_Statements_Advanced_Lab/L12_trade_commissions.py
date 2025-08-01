town = input()
sales = float(input())
commission_percentage = 0

if town == 'Sofia':
    if sales < 0:
        print('error')
    elif sales <= 500:
        commission_percentage = 5
    elif sales <= 1000:
        commission_percentage = 7
    elif sales <= 10000:
        commission_percentage = 8
    elif sales > 10000:
        commission_percentage = 12
elif town == 'Varna':
    if sales < 0:
        print('error')
    elif sales <= 500:
        commission_percentage = 4.5
    elif sales <= 1000:
        commission_percentage = 7.5
    elif sales <= 10000:
        commission_percentage = 10
    elif sales > 10000:
        commission_percentage = 13
elif town == 'Plovdiv':
    if sales < 0:
        print('error')
    elif sales <= 500:
        commission_percentage = 5.5
    elif sales <= 1000:
        commission_percentage = 8
    elif sales <= 10000:
        commission_percentage = 12
    elif sales > 10000:
        commission_percentage = 14.5
    else:
        print('error')
else:
    print('error')

if commission_percentage > 0:
    commission = sales * commission_percentage / 100
    print(f'{commission:.2f}')