numbers = [int(n) for n in input().split()]
avg = sum(numbers) / len(numbers)

result = sorted([n for n in numbers if n > avg], reverse=True)[:5]

result_as_string = " ".join(str(n) for n in result)

print(result_as_string or "No")