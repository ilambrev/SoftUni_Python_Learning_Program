students = {}

input_line = input()

while ":" in input_line:
    name, id, course = input_line.split(":")
    students[id] = {"name": name, "course": course}

    input_line = input()

for id, info in students.items():
    course = input_line.replace("_", " ")
    if info["course"] == course:
        print(f"{info['name']} - {id}")