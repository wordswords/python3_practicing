#!/usr/bin/env python3

from Board import Board
from AI import TicTacToeAI
from TicTacToeScorer import TicTacToeScorer

class TicTacToe():
    """A Tic Tac Toe game."""

    boardclass = Board()
    board = boardclass.board
    player = boardclass.player
    computer = boardclass.computer
    ai = TicTacToeAI(boardclass)

    def get_user_move(self, board):
        """Get a move from the user."""

        while True:
            row_str = input('Enter row: ')
            col_str = input('Enter column: ')
            if self.validate_user_move(row_str, col_str, board):
                break
        return int(row_str)-1, int(col_str)-1


    def play_game(self):
        """Play a game of Tic Tac Toe."""

        TicTacToeScorer.mark_print(self.board)
        while True:
            row, col = self.get_user_move(self.board)
            self.board[row][col] = self.player
            print('Your move:')
            TicTacToeScorer.mark_print(self.board)
            if TicTacToeScorer.mark_score(self.board) != None:
                break
            [row, col] = TicTacToeScorer.get_next_computer_move(self.board, self.ai)
            if row == -1 and col == -1:
                print('No more moves for CPU!')
                break
            self.board[row][col] = self.computer
            print('CPU move:')
            TicTacToeScorer.mark_print(self.board)
            if TicTacToeScorer.mark_score(self.board) != None:
                break
        print(TicTacToeScorer.mark_score(self.board))

    def validate_user_move(self, row_str, col_str, board):
        """Check if the input is valid."""

        try:
            row = int(row_str)
            col = int(col_str)
        except ValueError:
            print('Invalid input')
            return False

        if type(row) != int or type(col) != int:
            print('Invalid input')
            return False
        if row not in range(1, 4) or col not in range(1, 4):
            print('Invalid input')
            return False
        if board[row-1][col-1] != ' ':
            print('That square is already taken.')
            return False
        return True

if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.play_game()
