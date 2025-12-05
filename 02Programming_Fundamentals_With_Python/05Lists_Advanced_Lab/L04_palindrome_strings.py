words = input().split()
palindrome = input()

palindromes = [word for word in words if word == word[::-1]]

palindrome_count = len([p for p in palindromes if p == palindrome])

print(palindromes)
print(f"Found palindrome {palindrome_count} times")