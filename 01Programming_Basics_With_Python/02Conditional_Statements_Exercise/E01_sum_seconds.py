first_competitor_time_in_sec = int(input())
second_competitor_time_in_sec = int(input())
third_competitor_time_in_sec = int(input())

total_time_in_sec = (first_competitor_time_in_sec
                     + second_competitor_time_in_sec
                     + third_competitor_time_in_sec)

minutes = total_time_in_sec // 60
seconds = total_time_in_sec % 60

if seconds < 10:
    print(f'{minutes}:{seconds:02d}')
else:
    print(f'{minutes}:{seconds}')