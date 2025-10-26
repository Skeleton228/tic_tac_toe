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


def restart_game():
    while True:
        game_data = {
            'board': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'current_player': 'X',
            'step': 1
        }
        print("=== КРЕСТИКИ-НОЛИКИ ===")
        print('\n' + '_' * 13)
        for i in range(board_size):
            print('|', game_data['board'][i * 3], '|', game_data['board'][1 + i * 3], '|',
                  game_data['board'][2 + i * 3], '|')
            print('-' * 13)

        while True:
            index = input(f"\nХодит игрок {game_data['current_player']}. Введите номер клетки (1-9): ")
            is_valid, message = validate_input(index, game_data['board'])
            if not is_valid:
                print(message)
                continue

            game_data['board'], game_data['current_player'] = game_rules(
                game_data['board'], int(index), game_data['current_player']
            )
            print('\n' + '_' * 13)
            for i in range(board_size):
                print('|', game_data['board'][i * 3], '|', game_data['board'][1 + i * 3], '|',
                      game_data['board'][2 + i * 3], '|')
                print('-' * 13)

            winner = check_win(game_data['board'])
            if winner:
                print('Победил игрок', winner)
                break

            if check_draw(game_data['board']):
                print("Ничья!")
                break

        response = input("\nХотите сыграть еще раз? (да/нет): ").lower()
        if response != 'да':
            print("\nСпасибо за игру! До свидания!")
            break


restart_game()
