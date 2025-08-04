days_off = int(input())

safe_playtime_per_year_in_minutes = 30000
time_to_play_on_work_day_in_minutes = 63
time_to_play_on_day_off_in_minutes = 127
days_in_one_year = 365

work_days = days_in_one_year - days_off

total_paly_time_in_minutes = (work_days
                              * time_to_play_on_work_day_in_minutes
                              + days_off
                              * time_to_play_on_day_off_in_minutes)

difference = safe_playtime_per_year_in_minutes - total_paly_time_in_minutes
hours = abs(difference) // 60
minutes = abs(difference) % 60

if difference >= 0:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')