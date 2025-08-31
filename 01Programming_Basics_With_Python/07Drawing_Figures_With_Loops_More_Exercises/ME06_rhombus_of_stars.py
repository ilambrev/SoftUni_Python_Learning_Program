n = int(input())

for i in range(1, n * 2):
    if i < n:
        print(f"{' ' * (n - i)}*{' *' * (i - 1)}")
    else:
        print(f"{' ' * (i - n)}*{' *' * (i - 1 - (i - n) * 2)}")