people = input().split()
k = int(input())

result = []
i = 0

while len(people) > 0:
    i = (i + k - 1) % len(people)
    result.append(people.pop(i))

print("[" + ",".join(result) + "]")