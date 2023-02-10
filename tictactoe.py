# Tic Tac Toe Scorer

def mark_sequence(board, mark, start_row, start_col, row_increment, col_increment):
    """Return True if mark occurs in a sequence of 3 on board starting at
    start_row, start_col and extending in the direction specified by
    row_increment and col_increment, and False otherwise."""
    for i in range(3):
        if board[start_row + i * row_increment][start_col + i * col_increment] != mark:
            return False
    return True

def mark_diagnoal(board, mark):
    """Return True if mark occurs in a diagonal sequence of 3 on board,
    and False otherwise."""
    return mark_sequence(board, mark, 0, 0, 1, 1) or mark_sequence(board, mark, 0, 2, 1, -1)

def mark_row(board, mark):
    """Return True if mark occurs in a row sequence of 3 on board,
    and False otherwise."""
    for row in range(3):
        if mark_sequence(board, mark, row, 0, 0, 1):
            return True
    return False

def mark_column(board, mark):
    """Return True if mark occurs in a column sequence of 3 on board,
    and False otherwise."""
    for col in range(3):
        if mark_sequence(board, mark, 0, col, 1, 0):
            return True
    return False

def mark_win(board, mark):
    """Return True if mark occurs in a sequence of 3 on board,
    and False otherwise."""
    return mark_diagnoal(board, mark) or mark_row(board, mark) or mark_column(board, mark)

def mark_tie(board):
    """Return True if board is full, and False otherwise."""
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    return True

def mark_score(board):
    """Return the score for board."""
    if mark_win(board, 'X'):
        print('X wins!')
        return 1
    elif mark_win(board, 'O'):
        print('O wins!')
        return -1
    elif mark_tie(board):
        print('It\'s a tie :(')
        return 0
    else:
        return None

def mark_print(board):
    """Print the board."""
    for row in range(3):
        for col in range(3):
            print('[' + board[row][col] + ']', end='')
        print()

def check_valid_move(row, col, board):
    """Check if the input is valid."""
    if row not in range(0, 3) or col not in range(0, 3):
        print('Invalid input')
        return False
    if board[row][col] != ' ':
        print('That square is already taken.')
        return False
    return True

def mark_get(board):
    """Get a move from the user."""
    while True:
        row = int(input('Enter row: ')) - 1
        col = int(input('Enter column: ')) - 1
        if check_valid_move(row, col, board):
            break
    return row, col

def mark_computer(board):
    """Return the computer's move."""
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return row, col

def mark_game():
    """Play a game of Tic Tac Toe."""
    board = [[' '] * 3 for i in range(3)]
    mark_print(board)
    while True:
        row, col = mark_get(board)
        board[row][col] = 'X'
        print('Your move:')
        mark_print(board)
        if mark_score(board) != None:
            break
        row, col = mark_computer(board)
        board[row][col] = 'O'
        print('CPU move:')
        mark_print(board)
        if mark_score(board) != None:
            break
    print(mark_score(board))

def mark_test():
    """Test the functions in this module."""
    board = [['X', 'X', 'X'],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    assert mark_win(board, 'X')
    assert not mark_win(board, 'O')
    assert not mark_diagnoal(board, 'X')
    assert not mark_diagnoal(board, 'O')
    assert mark_row(board, 'X')
    assert not mark_row(board, 'O')
    assert not mark_column(board, 'X')
    assert not mark_column(board, 'O')
    assert not mark_tie(board)
    assert mark_score(board) == 1
    board = [['X', 'O', 'X'],
             [' ', 'O', ' '],
             [' ', ' ', 'O']]
    assert not mark_win(board, 'O')
    assert not mark_win(board, 'X')
    assert not mark_diagnoal(board, 'X')
    assert not mark_diagnoal(board, 'O')
    assert not mark_row(board, 'X')
    assert not mark_row(board, 'O')
    assert not mark_column(board, 'X')
    assert not mark_column(board, 'O')
    board = [['X', 'O', 'X'],
             ['O', 'X', 'O'],
             ['O', 'X', 'X']]
    assert not mark_win(board, 'O')
    assert mark_win(board, 'X')
    assert mark_diagnoal(board, 'X')
    assert not mark_diagnoal(board, 'O')
    assert not mark_row(board, 'X')
    assert not mark_row(board, 'O')
    assert not mark_column(board, 'X')
    assert not mark_column(board, 'O')
    assert mark_score(board) == 1
    print('All tests passed.')


def mark_main():
    """Play a game of Tic Tac Toe."""
    mark_game()

def mark_test_main():
    """Test the functions in this module."""
    mark_test()

def mark_debug_main():
    """Test the functions in this module."""
    import pdb
    pdb.set_trace()
    mark_test()

def mark_profile_main():
    """Profile the functions in this module."""
    import cProfile
    cProfile.run('mark_test()')

if __name__ == '__main__':
    mark_test()
    mark_main()






