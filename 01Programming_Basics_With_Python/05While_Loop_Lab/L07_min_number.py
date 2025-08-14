from sys import maxsize

min_number = maxsize

while True:
    imput_line = input()

    if imput_line == 'Stop':
        break

    number = int(imput_line)

    if (number < min_number):
        min_number = number

print(min_number)