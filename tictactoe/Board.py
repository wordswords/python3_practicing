#!/usr/bin/env python3

from TicTacToeScorer import TicTacToeScorer

class Board():
    """The TTT Board object"""

    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player = 'X'
    computer = 'O'
    scorer = TicTacToeScorer


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

    def is_space_free(self, space):
        if self.board[space[0]][space[1]] == ' ':
            return True
        else:
            return False


