key = int(input())
lines = int(input())

message = ""

for _ in range(lines):
    symbol = input()
    message += chr(ord(symbol) + key)

print(message)