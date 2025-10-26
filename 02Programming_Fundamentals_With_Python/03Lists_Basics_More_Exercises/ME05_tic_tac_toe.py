board = [input().replace(" ", ""), input().replace(" ", ""), input().replace(" ", "")]

player_one_win_combination = "111"
player_two_win_combination = "222"
result = "Draw!"
combinations = [
    board[0], board[1], board[2],
    board[0][0] + board[1][0] + board[2][0],
    board[0][1] + board[1][1] + board[2][1],
    board[0][2] + board[1][2] + board[2][2],
    board[0][1] + board[1][1] + board[2][1],
    board[1][0] + board[1][1] + board[1][2],
    board[0][0] + board[1][1] + board[2][2],
    board[0][2] + board[1][1] + board[2][0]
]

if player_one_win_combination in combinations:
    result = "First player won"
elif player_two_win_combination in combinations:
    result = "Second player won"

print(result)