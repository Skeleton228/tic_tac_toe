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
