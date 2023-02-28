#!/usr/bin/env python3

from ../scorer import TicTacToeScorer

class Board():
    """The TTT Board object"""

    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player = 'X'
    computer = 'O'
    scorer = TicTacToeScorer.TicTacToeScorer


    def __init__(self, status=None, player=None, computer=None):
        """Initialize the board with a set status"""

        if player != None:
            self.player = player
        if computer != None:
            self.computer = computer

        if status is None:
            for x in range(0, 2):
                for y in range(0, 2):
                    self.board[x][y] = ' '
        else:
            self.board = status

    def is_winner(self, piece):
        return self.scorer.mark_win(self.board, piece)

