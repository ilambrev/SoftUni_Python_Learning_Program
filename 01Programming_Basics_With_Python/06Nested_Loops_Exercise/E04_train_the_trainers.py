jury_members_count = int(input())

presentation_count = 0
presentations_marks_sum = 0.0

input_line = input()

while input_line != 'Finish':
    presentation_marks_sum = 0.0
    presentation_title = input_line
    presentation_count += 1

    for _ in range(jury_members_count):
        mark = float(input())
        presentation_marks_sum += mark

    presentation_average_score = presentation_marks_sum / jury_members_count

    presentations_marks_sum += presentation_average_score

    print(f'{presentation_title} - {presentation_average_score:.2f}.')

    input_line = input()

final_assessment = presentations_marks_sum / presentation_count

print(f'Student\'s final assessment is {final_assessment:.2f}.')