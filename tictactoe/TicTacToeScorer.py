#!/usr/bin/env python3


class TicTacToeScorer():
    """A Tic Tac Toe game scorer"""

    @staticmethod
    def mark_sequence(board, mark, start_row, start_col, row_increment, col_increment):
        """Return True if mark occurs in a sequence of 3 on board starting at start_row, start_col and extending in the direction specified by row_increment and col_increment, and False otherwise."""
        for i in range(3):
            if board[start_row + i * row_increment][start_col + i * col_increment] != mark:
                return False
        return True

    @staticmethod
    def mark_diagnoal(board, mark):
        """Return True if mark occurs in a diagonal sequence of 3 on board, and False otherwise."""

        return TicTacToeScorer.mark_sequence(board, mark, 0, 0, 1, 1) or TicTacToeScorer.mark_sequence(board, mark, 0, 2, 1, -1)

    @staticmethod
    def mark_row(board, mark):
        """Return True if mark occurs in a row sequence of 3 on board, and False otherwise."""

        for row in range(3):
            if TicTacToeScorer.mark_sequence(board, mark, row, 0, 0, 1):
                return True
        return False

    @staticmethod
    def mark_column(board, mark):
        """Return True if mark occurs in a column sequence of 3 on board, and False otherwise."""

        for col in range(3):
            if TicTacToeScorer.mark_sequence(board, mark, 0, col, 1, 0):
                return True
        return False

    @staticmethod
    def mark_win(board, piece):
        """Return True if mark occurs in a sequence of 3 on self.board, and False otherwise."""

        return TicTacToeScorer.mark_diagnoal(board, piece) or TicTacToeScorer.mark_row(board, piece) or TicTacToeScorer.mark_column(board, piece)

    @staticmethod
    def mark_tie(board):
        """Return True if self.board is full, and False otherwise."""

        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    return False
        return True

    @staticmethod
    def mark_score(board):
        """Return the score for self.board."""

        if TicTacToeScorer.mark_win(board, 'X'):
            #print('X wins!')
            return 1
        elif TicTacToeScorer.mark_win(board, 'O'):
            #print('O wins!')
            return -1
        elif TicTacToeScorer.mark_tie(board):
            #print('It\'s a tie :(')
            return 0
        else:
            return None

    @staticmethod
    def mark_print(board):
        """Print the board."""

        for row in range(3):
            for col in range(3):
                print('('+str(row+1)+','+str(col+1)+')[ -' + board[row][col] + '- ] ', end='')
            print()

    @staticmethod
    def get_next_computer_move(board, ai):
        """Return the computer's move."""

        move = ai.get_best_move(board)
        if move == None:
            return -1, -1
        else:
            return move[0], move[1]

