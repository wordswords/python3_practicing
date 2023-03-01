#!/usr/bin/env python3

from Board import Board
from TicTacToeScorer import TicTacToeScorer

class TicTacToeAI():
    """An optimal AI for the TicTacToe game that always plays a perfect game"""

    boardclass = Board()
    board = None
    player = ''
    computer = ''

    def __init__(self, boardclass):
        self.boardclass = boardclass
        self.board = self.boardclass.board
        self.player = self.boardclass.player
        self.computer = self.boardclass.computer

    def make_move(self, x, y, piece):
        """ Makes a move on the board """

        self.board[x][y] = piece # type: ignore[attr-defined]

    def get_winning_moves(self, board, piece):
        """
        Returns a list of all moves that will result in the computer winning
        """
        #import ipdb;ipdb.set_trace()

        moves = []
        for x in range(0, 3):
            for y in range(0, 3):
                if self.boardclass.is_space_free([x,y]):
                    self.make_move(x,y, piece)
                    if TicTacToeScorer.mark_win(board, piece):
                        moves.append([x,y])
                    self.make_move(x,y, ' ')

        return moves

    def get_blocking_moves(self, board, piece):
        """
        Returns a list of all moves that will block the player from winning
        """
        moves = []
        for x in range(0, 3):
            for y in range(0, 3):
                if self.boardclass.is_space_free([x,y]):
                    self.make_move(x,y, self.player)
                    if TicTacToeScorer.mark_win(board, self.player):
                        moves.append([x,y])
                    self.make_move(x,y, ' ')
        return moves

    def get_fork_moves(self, board, piece):
        """
        Returns a list of all moves that will create a fork
        """
        moves = []
        for x in range(0, 3):
            for y in range(0, 3):
                if self.boardclass.is_space_free([x,y]):
                    self.make_move(x,y, piece)
                    if len(self.get_winning_moves(board, piece)) > 1:
                        moves.append([x,y])
                    self.make_move(x,y, ' ')
        return moves

    def get_block_fork_moves(self, board, piece):
        """
        Returns a list of all moves that will block the fork
        """
        moves = []
        for x in range(0, 3):
            for y in range(0, 3):
                if self.boardclass.is_space_free([x,y]):
                    self.make_move(x,y, self.player)
                    if len(self.get_fork_moves(board, self.player)) > 1:
                        moves.append([x,y])
                    self.make_move(x,y, ' ')
        return moves

    def get_center_moves(self, board):
        """
        Returns a list of all moves that will take the center
        """
        moves = []
        if self.boardclass.is_space_free([1,1]):
            moves.append([1,1])
        return moves

    def get_opposite_corner_moves(self, board):
        """
        Returns a list of all moves that will take the opposite corner
        """
        moves = []
        if self.boardclass.is_space_free([2,2]):
            if self.boardclass.is_space_free([0,0]):
                moves.append([2,2])
        elif self.boardclass.is_space_free([2,0]):
            if self.boardclass.is_space_free([0,2]):
                moves.append([2,0])
        elif self.boardclass.is_space_free([0,1]):
            if self.boardclass.is_space_free([2,2]):
                moves.append([0,0])
        elif self.boardclass.is_space_free([0,2]):
            if self.boardclass.is_space_free([2,0]):
                moves.append([0,2])
        return moves

    def get_side_moves(self, board):
        """
        Returns a list of all moves that will take a side spot
        """
        moves = []
        for i in [[0,1],[1,0],[1,2],[2,1]]:
            if self.boardclass.is_space_free(i):
                moves.append(i)
        return moves

    def get_corner_moves(self, board):
        """
        Returns a list of all moves that will take a corner
        """
        moves = []
        for i in [[0,0],[0,2],[2,0],[2,2]]:
            if self.boardclass.is_space_free(i):
                moves.append(i)
        return moves

    def get_best_move(self, board):
        """
        Returns the best move according to the above rules
        """

        self.board = board

        # if we can win, make that move
        for move in self.get_winning_moves(self.board, self.computer):
            return move
        # if the player could win, block that move
        for move in self.get_blocking_moves(self.board, self.player):
            return move
        # check for forks
        for move in self.get_fork_moves(self.board, self.computer):
            return move
        # check for forks to block
        for move in self.get_block_fork_moves(self.board, self.player):
            return move
        # take the center if it is free
        for move in self.get_center_moves(self.board):
            return move
        # take any of the opposite corners if they are free
        for move in self.get_opposite_corner_moves(self.board):
            return move
        # take any of the available sides
        for move in self.get_side_moves(self.board):
            return move
        # take any of the available corners
        for move in self.get_corner_moves(self.board):
            return move

