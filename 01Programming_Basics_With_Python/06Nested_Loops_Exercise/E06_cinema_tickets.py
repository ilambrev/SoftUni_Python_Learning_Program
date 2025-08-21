student_tickets = 0
standard_tickets = 0
kid_tickets = 0

input_line = input()

while input_line != 'Finish':
    movie_title = input_line
    free_sits = int(input())

    taken_seats = 0

    input_line = input()

    while input_line != 'End':
        taken_seats += 1

        if input_line == 'student':
            student_tickets += 1
        elif input_line == 'standard':
            standard_tickets += 1
        elif input_line == 'kid':
            kid_tickets += 1

        if taken_seats == free_sits:
            break

        input_line = input()

    taken_seats_percentage = 100 * taken_seats / free_sits

    print(f'{movie_title} - {taken_seats_percentage:.2f}% full.')

    input_line = input()

total_tickets = (student_tickets
                 + standard_tickets
                 + kid_tickets)

student_tickets_percentage = 100 * student_tickets / total_tickets
standard_tickets_percentage = 100 * standard_tickets / total_tickets
kid_tickets_percentage = 100 * kid_tickets / total_tickets

print(f'Total tickets: {total_tickets}')
print(f'{student_tickets_percentage:.2f}% student tickets.')
print(f'{standard_tickets_percentage:.2f}% standard tickets.')
print(f'{kid_tickets_percentage:.2f}% kids tickets.')