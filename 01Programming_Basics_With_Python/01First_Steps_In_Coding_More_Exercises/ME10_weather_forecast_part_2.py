degrees = float(input())

result = ''

if 5.0 <= degrees <= 11.9:
    result = 'Cold'
elif 12.0 <= degrees <= 14.9:
    result = 'Cool'
elif 15.0 <= degrees <= 20.0:
    result = 'Mild'
elif 20.1 <= degrees <= 25.9:
    result = 'Warm'
elif 26.00 <= degrees <= 35.0:
    result = 'Hot'
else:
    result = 'unknown'

print(result)