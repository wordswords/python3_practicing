#!/usr/bin/env python3

import Board
import TicTacToeScorer
import TicTacToe

class TicTacToeTest():
    """Test the functions in the self module."""
    

    def mark_test(self):
        """Test the functions in this module."""

        boardclass = Board.Board
        scorer = TicTacToeScorer.TicTacToeScorer

        boardtestone = boardclass([['X', 'X', 'X'],
                                           [' ', ' ', ' '],
                                           [' ', ' ',' ']],
                                           'X', 'O')
        board = boardtestone.board

        repr(scorer.mark_win(board, 'X'))
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

        boardtesttwo = boardclass([['X', 'O', 'X'],
                                    [' ', 'O', ' '],
                                    [' ', ' ', 'O']], 
                                    'X', 'O')

        board = boardtesttwo.board
        assert not scorer.mark_win(board, 'O')
        assert not scorer.mark_win(board, 'X')
        assert not scorer.mark_diagnoal(board, 'X')
        assert not scorer.mark_diagnoal(board, 'O')
        assert not scorer.mark_row(board, 'X')
        assert not scorer.mark_row(board, 'O')
        assert not scorer.mark_column(board, 'X')
        assert not scorer.mark_column(board, 'O')

        boardtestthree = boardclass([['X', 'O', 'X'],
                                    [' ', 'O', ' '],
                                    [' ', 'X', 'X']], 
                                    'X', 'O')
        board = boardtestthree.board

        assert not scorer.mark_win(board, 'O')
        assert not scorer.mark_win(board, 'X')
        assert not scorer.mark_diagnoal(board, 'X')
        assert not scorer.mark_diagnoal(board, 'O')
        assert not scorer.mark_row(board, 'X')
        assert not scorer.mark_row(board, 'O')
        assert not scorer.mark_column(board, 'X')
        assert not scorer.mark_column(board, 'O')

        boardtestfour = boardclass([['X', 'O', 'X'],
                                    ['O', 'O', 'X'],
                                    ['X', 'O', 'O']], 
                                    'X', 'O')
        board = boardtestfour.board

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


