day_of_week = input()
message = ''

if day_of_week == 'Monday' or\
        day_of_week == 'Tuesday' or\
        day_of_week == 'Wednesday' or\
        day_of_week == 'Thursday' or\
        day_of_week == 'Friday':
    message = 'Working day'
elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    message = 'Weekend'
else:
    message = 'Error'

print(message)