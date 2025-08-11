from math import floor

tournaments_number = int(input())
rank_list_scores = int(input())

winer_scores = 2000
finalist_scores = 1200
semi_finalist_scores = 720

wins_count = 0
tournaments_scores = 0

for _ in range(tournaments_number):
    tournament_stage = input()

    if tournament_stage == 'W':
        tournaments_scores += winer_scores
        wins_count += 1
    elif tournament_stage == 'F':
        tournaments_scores += finalist_scores
    elif tournament_stage == 'SF':
        tournaments_scores += semi_finalist_scores

rank_list_scores += tournaments_scores
average_scores = tournaments_scores / tournaments_number
wins_percentage = 100 * wins_count / tournaments_number

print(f'Final points: {rank_list_scores}')
print(f'Average points: {floor(average_scores)}')
print(f'{wins_percentage:.2f}%')