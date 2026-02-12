distances = [int(d) for d in input().split()]

sum = 0

while distances:
    index = int(input())
    removed_elemen = 0

    if index < 0:
        removed_elemen = distances[0]
        sum += removed_elemen
        distances[0] = distances[-1]
    elif index > len(distances) - 1:
        removed_elemen = distances[-1]
        sum += removed_elemen
        distances[-1] = distances[0]
    else:
        removed_elemen = distances.pop(index)
        sum += removed_elemen
    
    distances = [d + removed_elemen if d <= removed_elemen else d - removed_elemen for d in distances]

print(sum)