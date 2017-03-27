

def Board(player, opponent):
    Player = player
    Opponent = opponent
    board = [1,2,3,4,5,6,7,8,9]
    winning_combinations = (((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)))

    def draw_board():
        print(board[6],"|", board[7],"|", board[8])
        print("-----")
        print(board[3],"|", board[4],"|", board[5])
        print("-----")
        print(board[0],"|", board[1],"|", board[2])
        print()

    def check_board():
        count = 0
        for a in winning_combinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Player Wins!\n")
                print("Congratulations!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Computer Wins\n")
                print("Better luck next tim :(\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True