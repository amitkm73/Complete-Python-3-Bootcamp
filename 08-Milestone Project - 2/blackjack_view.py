"""
user interface class for blackjack game
"""


class BlackjackView:
    """
    currently implemented as text
    can be replaced with GUI at a later stage
    """
    def __init__(self):
        pass

    @staticmethod
    def show_game_start():
        """
        :return: None
        """
        print('**** welcome to blackjack ****')

    @staticmethod
    def show_player(player):
        """
        :param player:
        :return: None
        """
        print(f'[{player.name}]: balance = {player.balance}')

    @staticmethod
    def show_round_start(bank):
        """
        :return: None
        """
        print('*' * 80)
        print(f'**** starting a new round of Blackjack; money in the bank = {bank} ****')

    @staticmethod
    def show_hand(player):
        """
        :return: None
        """
        text = '[' + player.name + ']:\t'
        for card in player.hand:
            text = text + card.__str__() + ' | '
        print(text)

    @staticmethod
    def get_move():
        """
        :return: h for hit and s for stay according to human player input
        """
        move = ''
        while move not in ['h', 's']:
            move = input('your move please; select [h]it or [s]tay:  ').lower()
        return move

    @staticmethod
    def show_move(player, move):
        """
        :param player:
        :param move:
        :return: None
        """
        print(f'[{player.name}]:\tmove = [{move}] ')

    @staticmethod
    def show_busted(player):
        """
        :param player:
        :param move:
        :return: None
        """
        print(f'[{player.name}]:\tBUSTED !')

    @staticmethod
    def show_round_finish(game, winner):
        """
        :param game:
        :param player:
        :return: None
        """
        print(f'[{winner.name}]:\twins the round, score = {game.score(winner)}')
        for player in game.players:
            BlackjackView.show_player(player)
        print('*'*80)

    @staticmethod
    def get_bet():
        """
        :return: bet as selected by the user, must be a positive integer
        """
        bet = 0
        while bet <= 0:
            try:
                input_str = input('place your bet: ')
                bet = int(input_str)
            except ValueError:
                continue
        return bet

    @staticmethod
    def get_next_round():
        """
        :return: True if user wants to play another round, False otherwise
        """
        selection = ''
        while selection not in ['y', 'n']:
            selection = input('do you want to play another round? select [y]es or [n]o:  ').lower()
        return selection == 'y'

    @staticmethod
    def show_goodbye():
        """
        :return: None
        """
        print('**** thanks for playing Blackjack - see you again soon ****')
