n = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for _ in range(n):
    number = int(input())
    if number < 200:
        p1_count += 1
    elif number < 400:
        p2_count += 1
    elif number < 600:
        p3_count += 1
    elif number < 800:
        p4_count += 1
    elif number >= 800:
        p5_count += 1

p1_percentage = 100 * p1_count / n
p2_percentage = 100 * p2_count / n
p3_percentage = 100 * p3_count / n
p4_percentage = 100 * p4_count / n
p5_percentage = 100 * p5_count / n

print(f'{p1_percentage:.2f}%')
print(f'{p2_percentage:.2f}%')
print(f'{p3_percentage:.2f}%')
print(f'{p4_percentage:.2f}%')
print(f'{p5_percentage:.2f}%')