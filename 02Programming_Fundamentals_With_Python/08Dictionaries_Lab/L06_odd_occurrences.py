words = [w.lower() for w in input().split()]

words_occurrences = {}

for word in words:
    if word not in words_occurrences:
        words_occurrences[word] = 0
    
    words_occurrences[word] += 1

print(" ".join([w for w in words_occurrences if not words_occurrences[w] % 2 == 0]))