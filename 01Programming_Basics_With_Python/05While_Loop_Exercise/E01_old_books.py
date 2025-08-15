wanted_book = input()

isWantedBookFound = False
checked_books = 0

while True:
    input_data = input()

    if input_data == 'No More Books':
        break

    if input_data == wanted_book:
        isWantedBookFound = True
        break

    checked_books += 1

if isWantedBookFound:
    print(f'You checked {checked_books} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {checked_books} books.')