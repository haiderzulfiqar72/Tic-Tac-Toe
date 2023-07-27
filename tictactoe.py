"""
Tic Tac Toe Player
"""
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.if value == None:
    """
    x_count = sum([row.count(X) for row in board])
    o_count = sum([row.count(O) for row in board])
    if x_count <= o_count:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Exception Raised - Invalid action for the board")
    i, j = action
    new_board = copy.deepcopy(board)
    current_player = player(board)
    new_board[i][j] = current_player
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][0] is not None:
        return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

# def minimax(board):
    
#     return list(actions(board))[random.randint(0, len(actions(board))-1)]

def minimax_helper(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None, utility(board)

    player_sym = player(board)
    if player_sym == X:
        best_value = float('-inf')
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            _, value = minimax_helper(new_board)
            if value > best_value:
                best_value = value
                best_action = action
        return best_action, best_value
    else:
        best_value = float('inf')
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            _, value = minimax_helper(new_board)
            if value < best_value:
                best_value = value
                best_action = action
        return best_action, best_value
    
def minimax(board):
    return minimax_helper(board)[0]


b=[['X', 'X', 'X'], [None, None, None], [None, None, None]]
b=[['O', 'O', 'O'], [None, None, None], [None, None, None]]
b=[['X', None, None], ['X', None, None], ['X', None, None]]
b=[['O', None, None], ['O', None, None], ['O', None, None]]
b=[['X', None, None], [None, 'X', None], [None, None, 'X']]
b=[['O', None, None], [None, 'O', None], [None, None, 'O']]
b=[['O', 'X', 'O'], ['X', 'O', 'X'], ['X', 'O', 'X']]
b=[[None, None, None], [None, None, None], [None, None, None]]
b=[[None, 'X', 'O'], [None, None, None], [None, None, None]]
b=[[None, 'X', 'O'], [None, 'O', 'X'], [None, None, None]]
b=[[None, None, None], [None, None, None], [None, None, 'X']]
