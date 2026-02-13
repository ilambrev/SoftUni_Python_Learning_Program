people_count = int(input())
lift = [int(w) for w in input().split()]

while people_count > 0 and sum(lift) < len(lift) * 4:
    for i in range(len(lift)):
        if lift[i] < 4:
            lift[i] += 1
            people_count -= 1
            break

if people_count == 0 and sum(lift) < len(lift) * 4:
    print("The lift has empty spots!")
if people_count > 0 and sum(lift) == len(lift) * 4:
    print(f"There isn't enough space! {people_count} people in a queue!")

print(" ".join([str(w) for w in lift]))