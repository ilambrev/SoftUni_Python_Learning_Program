def determine_result_type(n1, n2, n3):
    if n1 == 0 or n2 == 0 or n3 == 0:
        return "zero"

    negative_numbers_count = 0

    if n1 < 0:
        negative_numbers_count += 1

    if n2 < 0:
        negative_numbers_count += 1

    if n3 < 0:
        negative_numbers_count += 1

    if negative_numbers_count % 2 == 0:
        return "positive"
    else:
        return "negative"

n1 = int(input())
n2 = int(input())
n3 = int(input())

print(determine_result_type(n1, n2, n3))