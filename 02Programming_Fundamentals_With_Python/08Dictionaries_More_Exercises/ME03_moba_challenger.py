players = {}

input_data = input()

while not input_data == "Season end":
    if ">" in input_data:
        player, position, skill = input_data.split(" -> ")
        skill = int(skill)

        if player not in players:
            players[player] = {}

        if position not in players[player]:
            players[player][position] = 0

        if players[player][position] < skill:
            players[player][position] = skill
    else:
        player1, player2 = input_data.split(" vs ")

        if player1 not in players or player2 not in players:
            input_data = input()
            continue

        for key in players[player1]:
            if key in players[player2]:
                if players[player1][key] > players[player2][key]:
                    players.pop(player2)
                elif players[player2][key] > players[player1][key]:
                    players.pop(player1)
                break

    input_data = input()

new_line = "\n"
players_ordered = ({k: {p: s for p, s in sorted(v.items(), key=lambda item: (-item[1], item[0]))} 
                    for k, v in sorted(players.items(), key=lambda item: (-sum(item[1].values()), item[0]))})

[print(f"{k}: {sum(v.values())} skill{new_line}{new_line.join(['- ' + p + ' <::> ' + str(s) for p, s in v.items()])}") for k, v in players_ordered.items()]