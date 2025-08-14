student_name = input()

grades_sum = 0.0
fail_grade_counter = 0
current_grade = 1

while True:
    grade = float(input())

    if grade >= 4:
        grades_sum += grade

        if current_grade < 12:
            current_grade += 1
        else:
            break
    else:
        fail_grade_counter += 1

    if fail_grade_counter >= 2:
        break    

if current_grade == 12:
    average_grade = grades_sum / 12
    print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
else:
    print(f'{student_name} has been excluded at {current_grade} grade')