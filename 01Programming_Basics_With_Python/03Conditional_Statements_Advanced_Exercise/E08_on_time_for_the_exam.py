exam_start_hour = int(input())
exam_start_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_start_time_in_minutes = exam_start_hour * 60 + exam_start_minute
arrival_time_in_minutes = arrival_hour * 60 + arrival_minute

status = ''

difference = exam_start_time_in_minutes - arrival_time_in_minutes

if difference < 0:
    status = 'Late'
elif 0 <= difference <= 30:
    status = 'On time'
else:
    status = 'Early'

print(status)

if -60 < difference < 0:
    print(f'{-difference} minutes after the start')
elif difference <= -60:
    hours = -difference // 60
    minutes = -difference % 60
    print(f'{hours}:{minutes:02d} hours after the start')
elif 0 < difference < 60:
    print(f'{difference} minutes before the start')
elif difference >= 60:
    hours = difference // 60
    minutes = difference % 60
    print(f'{hours}:{minutes:02d} hours before the start')