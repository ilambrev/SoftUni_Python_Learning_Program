cards_sequence = input()

cards = cards_sequence.split()
team_a_players = [0] * 11
team_b_players = [0] * 11
team_a_players_count = 11
team_b_players_count = 11
is_game_terminated = False

for card in cards:
    team, player = card.split("-")

    if team == 'A' and team_a_players[int(player) - 1] == 0:
        team_a_players[int(player) - 1] = 1
        team_a_players_count -= 1
    elif team == 'B' and team_b_players[int(player) - 1] == 0:
        team_b_players[int(player) - 1] = 1
        team_b_players_count -= 1

    if team_a_players_count < 7 or team_b_players_count < 7:
        is_game_terminated = True
        break

print(f"Team A - {team_a_players_count}; Team B - {team_b_players_count}")

if is_game_terminated:
    print("Game was terminated")