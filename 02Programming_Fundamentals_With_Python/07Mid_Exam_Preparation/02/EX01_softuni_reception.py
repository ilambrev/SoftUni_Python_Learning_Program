from math import ceil

empl1_capacity = int(input())
empl2_capacity = int(input())
empl3_capacity = int(input())
students_count = int(input())

total_capacity_per_hour = empl1_capacity + empl2_capacity + empl3_capacity

hours_needed = ceil(students_count / total_capacity_per_hour)

if students_count > 0:
    hours_needed += int(hours_needed / 3) - 1 if hours_needed % 3 == 0 else int(hours_needed / 3)

print(f"Time needed: {hours_needed}h.")