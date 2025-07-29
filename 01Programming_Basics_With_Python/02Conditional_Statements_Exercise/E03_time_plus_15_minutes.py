hour = int(input())
minutes = int(input())

if minutes + 15 > 59:
    hour += 1
    minutes = minutes + 15 - 60
else:
    minutes += 15

if hour == 24:
    hour = 0

print(f'{hour}:{minutes:02d}')