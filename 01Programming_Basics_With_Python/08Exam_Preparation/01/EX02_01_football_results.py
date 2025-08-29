wins = 0
losses = 0
draws = 0

first_match_result = input()

home_team_score = int(first_match_result[0])
guest_team_score = int(first_match_result[2])

if home_team_score > guest_team_score:
    wins += 1
elif home_team_score < guest_team_score:
    losses += 1
else:
    draws += 1

second_match_result = input()

home_team_score = int(second_match_result[0])
guest_team_score = int(second_match_result[2])

if home_team_score > guest_team_score:
    wins += 1
elif home_team_score < guest_team_score:
    losses += 1
else:
    draws += 1

third_match_result = input()

home_team_score = int(third_match_result[0])
guest_team_score = int(third_match_result[2])

if home_team_score > guest_team_score:
    wins += 1
elif home_team_score < guest_team_score:
    losses += 1
else:
    draws += 1

print(f'Team won {wins} games.')
print(f'Team lost {losses} games.')
print(f'Drawn games: {draws}')