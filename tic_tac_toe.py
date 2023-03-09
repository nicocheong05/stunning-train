X_won = 0               # variables to keep track of wins
O_won = 0
draw = 0


winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),(1, 4, 7), (2, 5, 8), (3, 6, 9),(1, 5, 9), (3, 5, 7)]


def X(x):
    next_X = int(moves[x])
    # print("X is placed in grid " + str(next_X))
    X_moves.append(next_X)
    # print(X_moves)
    x += 1
    return x


def O(o):
    next_O = int(moves[o])
    # print("O is placed in grid " + str(next_O))
    O_moves.append(next_O)
    # print(O_moves)
    o += 1
    return o


def check_win(player_list):
    for each_combo in winning_combinations:
        if all(item in player_list for item in each_combo):
            # print("checking...")
            return True
    return False


f = open("toe", "r")
while True:
    file_data = f.readline().strip()
    X_moves = []
    O_moves = []
    i = 0
    winner = ""                  # winner can either be X or O
    if file_data == "":
        break
    moves = file_data.split()
    while i < len(moves) - 1:
        i = X(i)
        if check_win(X_moves):
            winner = "X"
            break
        i = O(i)
        if check_win(O_moves):
            winner = "O"
            break
    if winner == "":
        i = X(i)
        if check_win(X_moves):
            X_won += 1
            print("WINNER IS X.")
        else:
            draw += 1
            print("DRAW.")
    elif winner == "X":
        X_won += 1
        print("WINNER IS X.")
    elif winner == "O":
        O_won += 1
        print("WINNER IS O.")
f.close()

print(X_won, O_won, draw)
a = X_won * O_won
b = a * draw
print(b)