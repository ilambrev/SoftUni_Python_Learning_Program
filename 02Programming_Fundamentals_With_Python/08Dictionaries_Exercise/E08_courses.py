courses = {}

input_data = input()

while not input_data == "end":
    course, student = input_data.split(" : ")

    if course not in courses:
        courses[course] = []
    
    courses[course].append(student)

    input_data = input()

new_line = "\n"
[print(f"{course}: {len(students)}{new_line}{new_line.join(['-- ' + s for s in students])}") for course, students in courses.items()]

# Old task condition for output:
#
# Print the courses with their names and total registered users, ordered by the count of registered users in descending order.
# For each contest print the registered users ordered by name in ascending order.
#
# Solution for output according to the old condition
#
# courses_sorted = {course: sorted(students) for course, students in sorted(courses.items(), key=lambda item: -len(item[1]))}
# [print(f"{course}: {len(students)}{new_line}{new_line.join(['-- ' + s for s in students])}") for course, students in courses_sorted.items()]