#!/usr/bin/env python3

class TicTacToe():
    """A Tic Tac Toe game."""

    board = Board.Board().board
    player = Board.Board().player
    computer = Board.Board().computer
    ai = AI.TicTacToeAI()
    scorer = TicTacToeScorer.TicTacToeScorer

    def mark_get(self, board):
        """Get a move from the user."""

        while True:
            row_str = input('Enter row: ')
            col_str = input('Enter column: ')
            if self.check_valid_move(row_str, col_str, board):
                break
        return int(row_str)-1, int(col_str)-1


    def mark_game(self):
        """Play a game of Tic Tac Toe."""

        self.scorer.mark_print(self.board)
        while True:
            row, col = self.mark_get(self.board)
            self.board[row][col] = self.player
            print('Your move:')
            self.scorer.mark_print(self.board)
            if self.scorer.mark_score(self.board) != None:
                break
            row, col = self.scorer.mark_computer(self.board, self.ai)
            if row == -1 and col == -1:
                print('No more moves for CPU!')
                break
            self.board[row][col] = self.computer
            print('CPU move:')
            self.scorer.mark_print(self.board)
            if self.scorer.mark_score(self.board) != None:
                break
        print(self.scorer.mark_score(self.board))

    def check_valid_move(cls, row_str, col_str, board):
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


    def mark_main(self):
        """Play a game of Tic Tac Toe."""

        self.mark_game()


if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.mark_main()
