days_count = int(input())
parking_hours_per_day = int(input())

total_sum = 0.0

for day in range(1, days_count + 1):
    day_sum = 0.0

    for hour in range(1, parking_hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            day_sum += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            day_sum += 1.25
        else:
            day_sum += 1.0

    total_sum += day_sum
    print(f'Day: {day} - {day_sum:.2f} leva')

print(f'Total: {total_sum:.2f} leva')