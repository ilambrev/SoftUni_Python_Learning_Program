students_count = int(input())

marks_between_2_00_and_2_99_count = 0
marks_between_3_00_and_3_99_count = 0
marks_between_4_00_and_4_99_count = 0
marks_between_5_00_and_6_00_count = 0
marks_sum = 0.0

for _ in range(students_count):
    student_mark = float(input())

    if student_mark < 3:
        marks_between_2_00_and_2_99_count += 1
    elif student_mark < 4:
        marks_between_3_00_and_3_99_count += 1
    elif student_mark < 5:
        marks_between_4_00_and_4_99_count += 1
    else:
        marks_between_5_00_and_6_00_count += 1

    marks_sum += student_mark

marks_between_2_00_and_2_99_percentage = 100 * \
    marks_between_2_00_and_2_99_count / students_count
marks_between_3_00_and_3_99_percentage = 100 * \
    marks_between_3_00_and_3_99_count / students_count
marks_between_4_00_and_4_99_percentage = 100 * \
    marks_between_4_00_and_4_99_count / students_count
marks_between_5_00_and_6_00_percentage = 100 * \
    marks_between_5_00_and_6_00_count / students_count
average_grade = marks_sum / students_count

print(f'Top students: {marks_between_5_00_and_6_00_percentage:.2f}%')
print(f'Between 4.00 and 4.99: {marks_between_4_00_and_4_99_percentage:.2f}%')
print(f'Between 3.00 and 3.99: {marks_between_3_00_and_3_99_percentage:.2f}%')
print(f'Fail: {marks_between_2_00_and_2_99_percentage:.2f}%')
print(f'Average: {average_grade:.2f}')