def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def evaluate(board):
    if check_winner(board, "X"):
        return 1
    elif check_winner(board, "O"):
        return -1
    else:
        return 0

def minimax(board, depth, maximizing_player):
    if check_winner(board, "X"):
        return 1
    elif check_winner(board, "O"):
        return -1
    elif check_draw(board):
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for move in get_available_moves(board):
            board[move[0]][move[1]] = "X"
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for move in get_available_moves(board):
            board[move[0]][move[1]] = "O"
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_eval = float("-inf")
    best_move = None
    for move in get_available_moves(board):
        board[move[0]][move[1]] = "X"
        eval = minimax(board, 0, False)
        board[move[0]][move[1]] = " "
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def main():
    board = initialize_board()
    print_board(board)

    while True:
        player_row, player_col = map(int, input("Enter your move (row column): ").split())
        if board[player_row][player_col] == " ":
            board[player_row][player_col] = "O"
        else:
            print("Invalid move. Try again.")
            continue

        print_board(board)

        if check_winner(board, "O"):
            print("You win!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("AI wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
