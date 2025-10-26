board_size = 3
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def validate_input(index, board):
    if not index.isdigit():
        return False, "Введите число от 1 до 9!"

    index_num = int(index)
    if index_num < 1 or index_num > 9:
        return False, "Число должно быть от 1 до 9!"

    if board[index_num - 1] in ('X', 'O'):
        return False, "Эта клетка уже занята!"

    return True, ""


def game_rules(board, index, player):
    board[index - 1] = player
    next_player = 'O' if player == 'X' else 'X'
    return board, next_player


def check_win(board):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c]:
            return board[a]
    return None


def check_draw(board):
    return all(cell in ('X', 'O') for cell in board) and check_win(board) is None
