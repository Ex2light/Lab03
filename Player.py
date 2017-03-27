from Make_A_Move import Make_A_Move

def Player(name, board):
    player_name = name
    player_mark = "O"
    board = board
    make_a_move = Make_A_Move()

    def choosing_next_move():
        n = make_a_move()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            choosing_next_move()
        else:
            board[n] = "O"

