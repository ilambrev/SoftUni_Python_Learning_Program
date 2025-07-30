day = int(input())
name = ''

if day == 1:
    name = 'Monday'
elif day == 2:
    name = 'Tuesday'
elif day == 3:
    name = 'Wednesday'
elif day == 4:
    name = 'Thursday'
elif day == 5:
    name = 'Friday'
elif day == 6:
    name = 'Saturday'
elif day == 7:
    name = 'Sunday'
else:
    name = 'Error'

print(name)