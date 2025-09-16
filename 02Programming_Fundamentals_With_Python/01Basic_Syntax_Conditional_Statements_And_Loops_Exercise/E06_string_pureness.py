n = int(input())

for _ in (range(n)):
    string = input()

    if string.find(',') == -1 and string.find('.') == -1 and string.find('_') == -1:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')