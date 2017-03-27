from Player import Player

def Starter(board):
    print("Welcome to the worst TicTacToe ever!!! \n")
    name = input("What's your name?")
    player = Player(name, board)

    return player