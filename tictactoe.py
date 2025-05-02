import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O

def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    if action not in actions(board):
        raise ValueError("Invalid action")
    i, j = action
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    return None

def terminal(board):
    return winner(board) is not None or all(EMPTY not in row for row in board)

def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0

def minimax(board):
    if terminal(board):
        return None
    
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    current_player = player(board)
    best_action = None
    
    if current_player == X:
        best_value = -math.inf
        for action in actions(board):
            move_value = min_value(result(board, action))
            if move_value > best_value:
                best_value = move_value
                best_action = action
    else:
        best_value = math.inf
        for action in actions(board):
            move_value = max_value(result(board, action))
            if move_value < best_value:
                best_value = move_value
                best_action = action
    
    return best_action