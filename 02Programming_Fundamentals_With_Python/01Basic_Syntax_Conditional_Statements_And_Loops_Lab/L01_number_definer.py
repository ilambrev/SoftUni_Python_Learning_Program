number = float(input())

message = ''

if number == 0:
    message = 'zero'
else:
    if abs(number) < 1:
        message += 'small '

    if abs(number) > 1_000_000:
        message += 'large '

    if number < 0:
        message += 'negative'

    if number > 0:
        message += 'positive'

print(message)