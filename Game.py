from Player import Player
from Opponent import Opponent
from Board import Board
from Starter import Starter

if __name__== "main":

    def TicTacToe():
        end_condition = False
        board = Board()
        starter = Starter(board)
        player = starter
        opponent = Opponent()

        while not end_condition:
            board.draw_board()
            end_condition = board.check_board()
            if end == True:
                break
            print("%s choose where to place a cross", player.player_name)
            player.choosing_next_move
            print()
            board.draw_board()
            end = board.check_board()
            if end == True:
                break
            opponent()
            print()

        if input("Play again (y/n)\n") == "y":
            print()
            TicTacToe()