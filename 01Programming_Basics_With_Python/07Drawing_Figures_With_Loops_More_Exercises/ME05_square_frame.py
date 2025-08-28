n = int(input())

print(f'+ {"- " * (n - 2)}+')

for _ in range(2, n):
    print(f'| {"- " * (n - 2)}|')

print(f'+ {"- " * (n - 2)}+')