#!/usr/bin/env python3

from tictactoe.board import Board
from tictactoe.scorer import TicTacToeScorer
from tictactoe import TicTacToe

class TicTacToeTest():
    """Test the functions in the self module."""
    

    def mark_test(self):
        """Test the functions in this module."""

        scorer = TicTacToeScorer.TicTacToeScorer

        board = Board.Board([['X', 'X', 'X'], 
                                    [' ', ' ', ' '], 
                                    [' ', ' ',' ']], 
                                    'X', 'O')

        assert scorer.mark_win(board, 'X')
        assert not scorer.mark_win(board, 'O')
        assert not scorer.mark_diagnoal(board, 'X')
        assert not scorer.mark_diagnoal(board, 'O')
        assert scorer.mark_row(board, 'X')
        assert not scorer.mark_row(board, 'O')
        assert not scorer.mark_column(board, 'X')
        assert not scorer.mark_column(board, 'O')
        assert not scorer.mark_tie(board)
        assert scorer.mark_score(board) == 1

        board = Board.Board([['X', 'O', 'X'],
                                    [' ', 'O', ' '],
                                    [' ', ' ', 'O']], 
                                    'X', 'O')
        assert not scorer.mark_win(board, 'O')
        assert not scorer.mark_win(board, 'X')
        assert not scorer.mark_diagnoal(board, 'X')
        assert not scorer.mark_diagnoal(board, 'O')
        assert not scorer.mark_row(board, 'X')
        assert not scorer.mark_row(board, 'O')
        assert not scorer.mark_column(board, 'X')
        assert not scorer.mark_column(board, 'O')

        board = Board.Board([['X', 'O', 'X'],
                                    [' ', 'O', ' '],
                                    [' ', 'X', 'X']], 
                                    'X', 'O')
        assert not scorer.mark_win(board, 'O')
        assert scorer.mark_win(board, 'X')
        assert scorer.mark_diagnoal(board, 'X')
        assert not scorer.mark_diagnoal(board, 'O')
        assert not scorer.mark_row(board, 'X')
        assert not scorer.mark_row(board, 'O')
        assert not scorer.mark_column(board, 'X')
        assert not scorer.mark_column(board, 'O')
        assert scorer.mark_score(board) == 1

        board = Board.Board([['X', 'O', 'X'],
                                    ['O', 'O', 'X'],
                                    ['X', 'O', 'O']], 
                                    'X', 'O')
        assert scorer.mark_win(board, 'O')
        assert not scorer.mark_win(board, 'X')
        assert not scorer.mark_diagnoal(board, 'X')
        assert not scorer.mark_diagnoal(board, 'O')
        assert not scorer.mark_row(board, 'X')
        assert not scorer.mark_row(board, 'O')
        assert not scorer.mark_column(board, 'X')
        assert scorer.mark_column(board, 'O')
        assert scorer.mark_score(board) == -1

        print('All tests passed.')


if __name__ == '__main__':
    selftest = TicTacToeTest()
    selftest.mark_test()


