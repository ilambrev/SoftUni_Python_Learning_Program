numbers = input().split()

left_racer_total_time = 0
right_racer_total_time = 0

for i in range(int(len(numbers) / 2)):
    left_racer_time = int(numbers[i])
    right_racer_time = int(numbers[-i - 1])

    if left_racer_time == 0:
        left_racer_total_time *= (100 - 20) / 100
    else:
        left_racer_total_time += left_racer_time

    if right_racer_time == 0:
        right_racer_total_time *= (100 - 20) / 100
    else:
        right_racer_total_time += right_racer_time

if left_racer_total_time < right_racer_total_time:
    print(f"The winner is left with total time: {left_racer_total_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_total_time:.1f}")