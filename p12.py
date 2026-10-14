def display(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True

        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False


board = [[" " for _ in range(3)] for _ in range(3)]
player = "X"

while True:
    display(board)

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if row not in range(3) or col not in range(3):
        print("Invalid position! Try again.")
        continue

    if board[row][col] != " ":
        print("Position already occupied! Try again.")
        continue

    board[row][col] = player

    if check_winner(board, player):
        display(board)
        print("Player", player, "wins!")
        break

    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        display(board)
        print("Match Draw!")
        break

    player = "O" if player == "X" else "X"
