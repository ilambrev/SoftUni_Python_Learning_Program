max_unsatisfactory_marks_count = int(input())

recieved_unsatisfactory_marks = 0
problems_count = 0
current_problem_name = ''
marks_sum = 0.0

while True:
    input_line = input()

    if input_line == 'Enough':
        break

    current_problem_name = input_line
    mark = float(input())
    marks_sum += mark
    problems_count += 1

    if mark <= 4:
        recieved_unsatisfactory_marks += 1

    if recieved_unsatisfactory_marks == max_unsatisfactory_marks_count:
        break

if recieved_unsatisfactory_marks == max_unsatisfactory_marks_count:
    print(f'You need a break, {recieved_unsatisfactory_marks} poor grades.')
else:
    average_score = marks_sum / problems_count
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {problems_count}')
    print(f'Last problem: {current_problem_name}')