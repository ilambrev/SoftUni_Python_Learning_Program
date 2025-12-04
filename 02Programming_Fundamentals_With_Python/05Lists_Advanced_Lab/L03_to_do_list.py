to_do_notes = []

command = input()

while not command == "End":
    level, note = command.split("-")
    to_do_notes.append([int(level), note])

    command = input()

print([note[1] for note in sorted(to_do_notes)])