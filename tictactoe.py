#!/usr/bin/env python3

class TicTacToe():
    board = []

    def mark_sequence(self, board, mark, start_row, start_col, row_increment, col_increment):
        """Return True if mark occurs in a sequence of 3 on self.board starting at start_row, start_col and extending in the direction specified by row_increment and col_increment, and False otherwise."""
        for i in range(3):
            if board[start_row + i * row_increment][start_col + i * col_increment] != mark:
                return False
        return True

    def mark_diagnoal(self, board, mark):
        """Return True if mark occurs in a diagonal sequence of 3 on self.board,
        and False otherwise."""
        return self.mark_sequence(board, mark, 0, 0, 1, 1) or self.mark_sequence(board, mark, 0, 2, 1, -1)

    def mark_row(self, board, mark):
        """Return True if mark occurs in a row sequence of 3 on self.board,
        and False otherwise."""
        for row in range(3):
            if self.mark_sequence(board, mark, row, 0, 0, 1):
                return True
        return False

    def mark_column(self, board, mark):
        """Return True if mark occurs in a column sequence of 3 on self.board,
        and False otherwise."""
        for col in range(3):
            if self.mark_sequence(board, mark, 0, col, 1, 0):
                return True
        return False

    def mark_win(self, board, mark):
        """Return True if mark occurs in a sequence of 3 on self.board,
        and False otherwise."""
        return self.mark_diagnoal(board, mark) or self.mark_row(board, mark) or self.mark_column(board, mark)

    def mark_tie(self, board):
        """Return True if self.board is full, and False otherwise."""
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    return False
        return True

    def mark_score(self, board):
        """Return the score for self.board."""
        if self.mark_win(board, 'X'):
            print('X wins!')
            return 1
        elif self.mark_win(board, 'O'):
            print('O wins!')
            return -1
        elif self.mark_tie(board):
            print('It\'s a tie :(')
            return 0
        else:
            return None

    def mark_print(self, board):
        """Print the board."""
        for row in range(3):
            for col in range(3):
                print('('+str(row+1)+','+str(col+1)+')[ -' + self.board[row][col] + '- ] ', end='')
            print()

    def check_valid_move(self, row_str, col_str, board):
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

    def mark_get(self, board):
        """Get a move from the user."""
        while True:
            row_str = input('Enter row: ')
            col_str = input('Enter column: ')
            if self.check_valid_move(row_str, col_str, board):
                break
        return int(row_str)-1, int(col_str)-1

    def mark_computer(self, board):
        """Return the computer's move."""
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    return row, col

        return -1,-1

    def mark_game(self):
        """Play a game of Tic Tac Toe."""
        self.board = [[' '] * 3 for i in range(3)]
        self.mark_print(self.board)
        while True:
            row, col = self.mark_get(self.board)
            self.board[row][col] = 'X'
            print('Your move:')
            self.mark_print(self.board)
            if self.mark_score(self.board) != None:
                break
            row, col = self.mark_computer(self.board)
            if row == -1 and col == -1:
                print('No more moves for CPU!')
                break
            self.board[row][col] = 'O'
            print('CPU move:')
            self.mark_print(self.board)
            if self.mark_score(self.board) != None:
                break
        print(self.mark_score(self.board))


    def mark_main(self):
        """Play a game of Tic Tac Toe."""
        self.mark_game()


class TicTacToeTest():

    def mark_profile_main(self,ttt):
        """Profile the functions in this module."""
        import cProfile
        cProfile.run('mark_test(ttt)')

    def mark_test(self,ttt):
        """Test the functions in this module."""
        board = [['X', 'X', 'X'],
                [' ', ' ', ' '],
                [' ', ' ', ' ']]
        assert ttt.mark_win(board, 'X')
        assert not ttt.mark_win(board, 'O')
        assert not ttt.mark_diagnoal(board, 'X')
        assert not ttt.mark_diagnoal(board, 'O')
        assert ttt.mark_row(board, 'X')
        assert not ttt.mark_row(board, 'O')
        assert not ttt.mark_column(board, 'X')
        assert not ttt.mark_column(board, 'O')
        assert not ttt.mark_tie(board)
        assert ttt.mark_score(board) == 1
        board = [['X', 'O', 'X'],
                [' ', 'O', ' '],
                [' ', ' ', 'O']]
        assert not ttt.mark_win(board, 'O')
        assert not ttt.mark_win(board, 'X')
        assert not ttt.mark_diagnoal(board, 'X')
        assert not ttt.mark_diagnoal(board, 'O')
        assert not ttt.mark_row(board, 'X')
        assert not ttt.mark_row(board, 'O')
        assert not ttt.mark_column(board, 'X')
        assert not ttt.mark_column(board, 'O')
        board = [['X', 'O', 'X'],
                ['O', 'X', 'O'],
                ['O', 'X', 'X']]
        assert not ttt.mark_win(board, 'O')
        assert ttt.mark_win(board, 'X')
        assert ttt.mark_diagnoal(board, 'X')
        assert not ttt.mark_diagnoal(board, 'O')
        assert not ttt.mark_row(board, 'X')
        assert not ttt.mark_row(board, 'O')
        assert not ttt.mark_column(board, 'X')
        assert not ttt.mark_column(board, 'O')
        assert ttt.mark_score(board) == 1
        board = [['X', 'O', 'X'],
                ['O', 'O', 'X'],
                ['X', 'O', 'O']]
        assert ttt.mark_win(board, 'O')
        assert not ttt.mark_win(board, 'X')
        assert not ttt.mark_diagnoal(board, 'X')
        assert not ttt.mark_diagnoal(board, 'O')
        assert not ttt.mark_row(board, 'X')
        assert not ttt.mark_row(board, 'O')
        assert not ttt.mark_column(board, 'X')
        assert ttt.mark_column(board, 'O')
        assert ttt.mark_score(board) == -1
        print('All tests passed.')


if __name__ == '__main__':
    ttt = TicTacToe()
    ttttest = TicTacToeTest()
    ttttest.mark_test(ttt)
    ttt.mark_main()


