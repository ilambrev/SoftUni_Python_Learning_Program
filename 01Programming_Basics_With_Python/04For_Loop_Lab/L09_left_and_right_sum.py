n = int(input())

left_sum = 0
right_sum = 0

for i in range(0, 2):
    for j in range(0, n):
        number = int(input())
        if i == 0:
            left_sum += number
        else:
            right_sum += number

if left_sum == right_sum:
    print('Yes, sum =', left_sum)
else:
    diff = abs(left_sum - right_sum)
    print('No, diff =', diff)