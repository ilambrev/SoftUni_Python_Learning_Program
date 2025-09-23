from math import ceil

people_count = int(input())
elevator_capacity = int(input())

elevator_courses = ceil(people_count / elevator_capacity)

print(elevator_courses)