n = int(input())

students = {}

for _ in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(grade)

studens_filtered = {name: sum(grades) / len(grades) for name, grades in students.items() if sum(grades) / len(grades) >= 4.5}

[print(f"{name} -> {average_grade:.2f}") for name, average_grade in studens_filtered.items()]

# Old task condition for output:
#
# When you finish reading the data, keep the students with average grade higher than or equal to 4.50.
# Order the filtered students by average grade in descending order.
#
# Solution for output according to the old condition
#
# studens_sorted = {name: grade for name, grade in sorted(
#     {k: sum(v) / len(v) for k, v in students.items() if sum(v) / len(v) >= 4.5}.items(), key=lambda item: -item[1])}
#
# [print(f"{name} -> {average_grade:.2f}") for name, average_grade in studens_sorted.items()]