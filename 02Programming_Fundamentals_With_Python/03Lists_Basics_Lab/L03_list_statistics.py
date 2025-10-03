n = int(input())

positive_numbers = []
negative_numbers = []

for _ in range(n):
    current_number = int(input())

    if current_number >= 0:
        positive_numbers.append(current_number)
    else:
        negative_numbers.append(current_number)

positives_count = len(positive_numbers)
negatives_sum = sum(negative_numbers)

print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {positives_count}\nSum of negatives: {negatives_sum}')