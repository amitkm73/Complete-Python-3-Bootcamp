# very basic tic tac toe; 3x3 hard coded board size; no classes, no gui, almost no exception handling
import random


def check_rows(game_board, mark):
    """
    :param game_board: 3 x 3 array of chars
    :param mark: character to check
    :return: True if mark appears 3 times in any row
    """
    for i in range(0, 3):
        if (game_board[i][0] == mark) and (game_board[i][1] == mark) and (game_board[i][2] == mark):
            return True
    return False


def check_cols(game_board, mark):
    """
    :param game_board: 3 x 3 array of chars
    :param mark: character to check
    :return: True if mark appears 3 times in any column
    """
    for j in range(0, 3):
        if (game_board[0][j] == mark) and (game_board[1][j] == mark) and (game_board[2][j] == mark):
            return True
    return False


def check_diags(game_board, mark):
    """
    :param game_board: 3 x 3 array of chars
    :param mark: character to check
    :return: True if mark appears in any of the diagonals
    """
    if (game_board[0][0] == mark) and (game_board[1][1] == mark) and (game_board[2][2] == mark):
        return True
    if (game_board[0][2] == mark) and (game_board[1][1] == mark) and (game_board[2][0] == mark):
        return True
    return False


def check_board(game_board, mark):
    """
    :param game_board: 3 x 3 array of chars
    :param mark: character to check
    :return: True if mark wins per tic tac toe game rules
    """
    return check_rows(game_board, mark) or check_cols(game_board, mark) or check_diags(game_board, mark)


def get_position(a, b):
    """
    :param a:  lower boundary
    :param b:  upper boundary
    :return: input from user in the range min .. max inclusive
    """
    choice = a-1
    while choice not in range(a, b+1):
        try:
            s = input(f'enter a number between {a} and {b}: ')
            choice = int(s)
        except ValueError:
            continue
    return choice


def get_choice(game_board, mark):
    """
    :param game_board: 3 x 3 array of chars
    :param mark: character for player prompt
    :return: row, col of valid choice (within board limits and not already taken)
    """
    valid_choice = False
    while not valid_choice:
        print(f'player {mark} enter row: ')
        row = get_position(0, 2)
        print(f'player {mark} enter column: ')
        col = get_position(0, 2)
        if game_board[row][col] == ' ':
            valid_choice = True
        else:
            print('slot already taken, try again')
            show_board(game_board)
    return row, col


def show_board(game_board):
    """
    :param game_board: 3 x 3 array of chars
    :return: None
    """
    print(f'-------------------')
    print(f'|  {game_board[0][0]}  |  {game_board[0][1]}  |  {game_board[0][2]}  |')
    print(f'-------------------')
    print(f'|  {game_board[1][0]}  |  {game_board[1][1]}  |  {game_board[1][2]}  |')
    print(f'-------------------')
    print(f'|  {game_board[2][0]}  |  {game_board[2][1]}  |  {game_board[2][2]}  |')
    print(f'-------------------')


def main():
    # Use a breakpoint in the code line below to debug your script.
    game_board = [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]
    player_mark = ('X', 'O')
    current_player = random.randint(0, 1)
    round_num = 1
    print(f'game is starting ... player {player_mark[current_player]} was randomly selected to go first !!!')
    while round_num <= 9:
        show_board(game_board)
        row, col = get_choice(game_board, player_mark[current_player])
        game_board[row][col] = player_mark[current_player]
        if check_board(game_board, player_mark[current_player]):
            print(f'player {player_mark[current_player]} wins !!!')
            show_board(game_board)
            break
        current_player = 1 - current_player
        round_num += 1
        pass
    if round_num == 10:
        show_board(game_board)
        print('no winner this time ... good bye')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
