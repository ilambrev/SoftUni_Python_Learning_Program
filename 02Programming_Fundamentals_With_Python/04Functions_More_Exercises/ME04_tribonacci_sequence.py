def tribonacci_sequence(n):
    sequence = [1] * n

    for i in range(2, n):
        sequence[i] = sum(sequence[max(i - 3, 0):i])

    print(*sequence)

n = int(input())

tribonacci_sequence(n)