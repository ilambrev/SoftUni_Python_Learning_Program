from sys import maxsize

max_number = -maxsize

while True:
    imput_line = input()

    if imput_line == 'Stop':
        break

    number = int(imput_line)

    if (number > max_number):
        max_number = number

print(max_number)