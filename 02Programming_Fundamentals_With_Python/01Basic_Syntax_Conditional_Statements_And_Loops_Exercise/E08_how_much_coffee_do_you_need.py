command = input()

coffees_counter = 0

while not command == 'END':
    if command == 'coding' or command == 'movie' or command == 'dog' or command == 'cat':
        coffees_counter += 1

    if command == 'CODING' or command == 'MOVIE' or command == 'DOG' or command == 'CAT':
        coffees_counter += 2

    command = input()

if coffees_counter <= 5:
    print(coffees_counter)
elif coffees_counter > 5:
    print('You need extra sleep')