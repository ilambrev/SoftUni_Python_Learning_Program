target_sum = int(input())

pay_in_cash = True
pay_in_cash_counter = 0
pay_in_cash_sum = 0
pay_with_card_counter = 0
pay_with_card_sum = 0

input_line = input()

while input_line != 'End':
    product_price = int(input_line)

    if pay_in_cash:
        if product_price <= 100:
            pay_in_cash_sum += product_price
            pay_in_cash_counter += 1
            print('Product sold!')
        else:
            print('Error in transaction!')
        pay_in_cash = False
    else:
        if product_price >= 10:
            pay_with_card_sum += product_price
            pay_with_card_counter += 1
            print('Product sold!')
        else:
            print('Error in transaction!')
        pay_in_cash = True

    if pay_in_cash_sum + pay_with_card_sum >= target_sum:
        average_cash_payment = pay_in_cash_sum / pay_in_cash_counter
        average_card_payment = pay_with_card_sum / pay_with_card_counter

        print(f'Average CS: {average_cash_payment:.2f}')
        print(f'Average CC: {average_card_payment:.2f}')

        break

    input_line = input()

else:
    print('Failed to collect required money for charity.')