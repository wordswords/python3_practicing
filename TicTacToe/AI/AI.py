#!/usr/bin/env python3

class TicTacToeAI():
    """An optimal AI for the TicTacToe game that always plays a perfect game"""
    def __init__(self):
        pass

    def get_move(self, board):
        # check if we can win in the next move
        for x in range(0, 2):
            for y in range(0, 2):
                if board.is_space_free([x,y]):
                    board.make_move([x,y], board.computer)
                    if board.is_winner(board.computer):
                        return [x,y]
                    # done checking this move, undo it
                    board.make_move([x,y], None)

        # check if the player could win on their next move
        for x in range(0, 2):
            for y in range(0, 2):
                if board.is_space_free([x,y]):
                    board.make_move([x,y], board.human)

                if board.is_winner(board.human):
                    return [x,y]
                # done checking this move, undo it
                board.make_move([x,y], None)

        # check if a corner is free
        for i in self.get_corner_moves(board):
            if board.is_space_free(i):
                return i

        # check if the middle is free
        if board.is_space_free([1,1]):
            return [1,1]

        # move on one of the sides
        for i in self.get_side_moves(board):
            if board.is_space_free(i):
                return i

    def get_winning_moves(self, board, piece):
        """
        Returns a list of all moves that will result in the computer winning
        """
        moves = []
        for x in range(0, 2):
            for y in range(0, 2):
                if board.is_space_free([x,y]):
                    board.make_move([x,y], piece)
                    if board.is_winner(piece):
                        moves.append([x,y])
                    board.make_move([x,y], piece)
        return moves

    def get_blocking_moves(self, board, piece):
        """
        Returns a list of all moves that will block the player from winning
        """
        moves = []
        for x in range(0, 2):
            for y in range(0, 2):
                if board.is_space_free([x,y]):
                    board.make_move([x,y], board.player)
                    if board.is_winner(piece):
                        moves.append([x,y])
                    board.make_move([x,y], piece)
        return moves

    def get_fork_moves(self, board, piece):
        """
        Returns a list of all moves that will create a fork
        """
        moves = []
        for x in range(0, 2):
            for y in range(0, 2):
                if board.is_space_free([x,y]):
                    board.make_move([x,y], piece)
                    if len(self.get_winning_moves(board, piece)) > 1:
                        moves.append([x,y])
                    board.make_move([x,y], piece)
        return moves

    def get_block_fork_moves(self, board, piece):
        """
        Returns a list of all moves that will block the fork
        """
        moves = []
        for i in range(1, 10):
            for x in range(0, 2):
                if board.is_space_free([x,y]):
                    board.make_move([x,y], board.player)
                    if len(self.get_fork_moves(board, board.player)) > 1:
                        moves.append([x,y])
                    board.make_move([x,y], piece)
        return moves

    def get_center_moves(self, board):
        """
        Returns a list of all moves that will take the center
        """
        moves = []
        if board.is_space_free(5):
            moves.append(5)
        return moves

    def get_opposite_corner_moves(self, board):
        """
        Returns a list of all moves that will take the opposite corner
        """
        moves = []
        if board.is_space_free([2,2]):
            if board.is_space_free([0,0]):
                moves.append([2,2])
        elif board.is_space_free([2,0]):
            if board.is_space_free([0,2]):
                moves.append([2,0])
        elif board.is_space_free([0,1]):
            if board.is_space_free([2,2]):
                moves.append([0,0])
        elif board.is_space_free([0,2]):
            if board.is_space_free([2,0]):
                moves.append([0,2])
        return moves

    def get_side_moves(self, board):
        """
        Returns a list of all moves that will take a side spot
        """
        moves = []
        for i in [[0,1],[1,0],[1,2],[2,1]]:
            if board.is_space_free(i):
                moves.append(i)
        return moves

    def get_corner_moves(self, board):
        """
        Returns a list of all moves that will take a corner
        """
        moves = []
        for i in [[0,0],[0,2],[2,0],[2,2]]:
            if board.is_space_free(i):
                moves.append(i)
        return moves

    def get_best_move(self, board):
        """
        Returns the best move according to the above rules
        """
        # if we can win, make that move
        for move in self.get_winning_moves(board, board.computer):
            return move
        # if the player could win, block that move
        for move in self.get_blocking_moves(board, board.human):
            return move
        # check for forks
        for move in self.get_fork_moves(board, board.computer):
            return move
        # check for forks to block
        for move in self.get_block_for_moves(board, board.human):
            return move
        # take the center if it is free
        for move in self.get_center_moves(board):
            return move
        # take any of the opposite corners if they are free
        for move in self.get_opposite_corner_moves(board):
            return move
        # take any of the available sides
        for move in self.get_side_moves(board):
            return move
        # take any of the available corners
        for move in self.get_corner_moves(board):
            return move

