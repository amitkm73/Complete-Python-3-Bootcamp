"""
blackjack game module
start with main_loop()
"""
import random
from abc import ABC, abstractmethod
from blackjack_view import BlackjackView

# some global constants
BLACKJACK = 21
BUST = -1
NUM_PLAYERS = 4


class Card:
    """
    Single Card
    """
    def __init__(self, suite, name, value):
        """
        :param suite: Clubs, Diamonds, Hearts, Spades
        :param name: Two, Three, ..., Jack, Queen, King, Ace
        :param value: 2, 3, ..., 11 for all face cards
        """
        self.suite = suite
        self.name = name
        self.value = value

    def __str__(self):
        """
        :return: string representation of the card, e.g 'Queen of Hearts'
        """
        return self.name + ' of ' + self.suite

    def get_value(self):
        """
        :return: value of the card
        """
        return self.value


class Deck:
    """
    Deck of cards
    """
    def __init__(self):
        """
        """
        self.cards = []
        for suite in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            for name, value in [('Two', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6),
                                ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10),
                                ('Jack', 10), ('Queen', 10), ('King', 10), ('Ace', 11)]:
                new_card = Card(suite, name, value)
                self.cards.append(new_card)

    def __str__(self):
        """
        :return: string representation of all cards in the deck, separated by newlines
        """
        text = ''
        for card in self.cards:
            text += card.__str__() + "\n"
        return text

    def shuffle(self):
        """
        :return: None
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        :return: top card in the deck
        """
        if len(self.cards) > 0:
            return self.cards.pop(0)
        return None


class Player(ABC):
    """
    blackjack player with a hand of cards and some money
    """
    def __init__(self, name, balance=0):
        """
        :param balance: amount of money entering the game
        """
        self.hand = []
        self.name = name
        self.balance = balance
        self.busted = False
        super().__init__()

    @abstractmethod
    def play(self):
        """
        :return: h for hit and s for stay
        """

    @abstractmethod
    def place_bet(self):
        """
        :return: amount of money to bet on the current round
        """


class HumanPlayer(Player):
    """
    human blackjack player
    """
    def play(self):
        """
        :return: h for hit and s for stay according to human player input
        """
        BlackjackView.show_hand(self)
        move = BlackjackView.get_move()
        BlackjackView.show_move(self, move)
        return move

    def place_bet(self):
        """
        :return: amount of money to bet on the current round
        """
        BlackjackView.show_player(self)
        bet = BlackjackView.get_bet()
        return bet


class Dealer(Player):
    """
    represents dealer's hand
    """
    def play(self):
        """
        :return: h for hit and s for stay according to stay <= 16 rule
        """
        BlackjackView.show_hand(self)
        points = BlackjackGame.score(self)
        if points <= 16:
            move = 'h'
        else:
            move = 's'
        BlackjackView.show_move(self, move)
        return move

    def place_bet(self):
        """
        :return: amount of money to bet on the current round
        """
        return 0


class BlackjackGame:
    """
    blackjack game with players, deck of cards, bets, multiple rounds, etc.
    in this flavor of blackjack dealer's hand is visible to all players
    in each round each player can hit or stay, until all stay or there's a winner
    warning: players can get into debt
    """
    def __init__(self):
        """
        """
        self.bank = 0               # holds the bets for the current round
        self.game_deck = Deck()     # full deck of cards
        # add the dealer and the human players:
        self.players = [Dealer('Dealer')]
        for i in range(0, NUM_PLAYERS-1):
            self.players.append(HumanPlayer('Player ' + str(i+1), 500))

    @staticmethod
    def score(player):
        """
        :param player: player to check
        :return: blackjack game score of the player's hand, -1 if BUST
        """
        score = 0
        for card in player.hand:
            score += card.get_value()
        # count aces as 1 instead of 11 if score is > 21
        if score > BLACKJACK:
            for card in player.hand:
                if card.get_value() == 11 and score > BLACKJACK:
                    score -= 10
        if score > BLACKJACK:
            score = BUST
        return score

    def execute_move(self, player, move):
        """
        :return: player score as result of the move
        """
        if move == 'h':
            player.hand.append(self.game_deck.deal())
            # TODO: handle a case where deck is empty
        BlackjackView.show_hand(player)
        score = BlackjackGame.score(player)
        return score

    def get_round_winner(self):
        """
        :return: player with score closest to 21
        """
        winner = self.players[0]
        for player in self.players:
            # note: score of BUST = -1
            if BlackjackGame.score(player) > BlackjackGame.score(winner):
                winner = player
        return winner

    def round(self):
        """
        play one round of blackjack, caller must deal with bets and card returns to game deck
        :return: player that is the winner of this round
        """
        # deal 2 cards for each player:
        BlackjackView.show_round_start(self.bank)
        self.game_deck.shuffle()
        for i in range(0, 2):
            for player in self.players:
                player.hand.append(self.game_deck.deal())
                player.busted = False
        for player in self.players:
            BlackjackView.show_hand(player)
        # check if one of the human players was dealt a BLACKJACK (and wins)
        for i in range(1, len(self.players)):
            if BlackjackGame.score(self.players[i]) == BLACKJACK:
                return self.players[i]
        # play continues until:
        # (1) everyone stays or (2) all players are BUSTed or (3) someone got a BLACKJACK
        remaining_players = len(self.players)
        all_stay = False
        while remaining_players > 1 and not all_stay:
            all_stay = True
            for player in self.players:
                if player.busted:
                    continue
                move = player.play()
                if move == 'h':
                    all_stay = False
                score = self.execute_move(player, move)
                if score == BLACKJACK:
                    # first player to reach 21 wins:
                    return player
                if score == BUST:
                    # remove player from the round and finish the round if needed:
                    player.busted = True
                    remaining_players -= 1
                    BlackjackView.show_busted(player)
                if remaining_players == 1:
                    break
        # select the winner - player not busted with score closest to BLACKJACK
        return self.get_round_winner()

    def main_loop(self):
        """
        main blackjack game loop
        :return: None
        """
        BlackjackView.show_game_start()
        another_round = True
        while another_round:
            for player in self.players:
                bet = player.place_bet()
                player.balance -= bet
                self.bank += bet
            self.bank = int(self.bank * 1.5)
            winner = self.round()
            winner.balance += self.bank
            self.bank = 0
            BlackjackView.show_round_finish(self, winner)
            for player in self.players:
                while len(player.hand) > 0:
                    self.game_deck.cards.append(player.hand.pop())
            another_round = BlackjackView.get_next_round()
        BlackjackView.show_goodbye()
