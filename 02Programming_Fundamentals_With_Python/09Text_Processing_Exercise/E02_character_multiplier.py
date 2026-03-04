str1, str2 = input().split()

result = 0

for i in range(0, max(len(str1), len(str2))):
    current_result = 1

    if i < len(str1):
        current_result *= ord(str1[i])

    if i < len(str2):
        current_result *= ord(str2[i])

    result += current_result

print(result)