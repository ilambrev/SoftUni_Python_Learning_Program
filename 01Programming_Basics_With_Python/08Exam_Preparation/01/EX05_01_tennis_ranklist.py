from math import floor

tournaments_count = int(input())
competitor_starting_points = int(input())

winner_points = 2000
finalist_points = 1200
semi_finalist_points = 720

earned_points = 0
wins = 0

for _ in range(tournaments_count):
    ranking = input()

    if ranking == 'W':
        wins += 1
        earned_points += winner_points
    elif ranking == 'F':
        earned_points += finalist_points
    elif ranking == 'SF':
        earned_points += semi_finalist_points

final_points = competitor_starting_points + earned_points
average_tournament_points = earned_points / tournaments_count
wins_percentage = 100 * wins / tournaments_count

print(f'Final points: {final_points}')
print(f'Average points: {floor(average_tournament_points)}')
print(f'{wins_percentage:.2f}%')