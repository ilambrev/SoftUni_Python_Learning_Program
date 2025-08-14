balance = 0.0

while True:
    input_line = input()

    if input_line == 'NoMoreMoney':
        break

    amount = float(input_line)

    if amount < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {amount:.2f}')
    balance += amount

print(f'Total: {balance:.2f}')