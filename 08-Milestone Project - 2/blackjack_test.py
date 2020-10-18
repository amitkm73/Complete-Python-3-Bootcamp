"""
unit tests for various blackjack game functions
does not cover all functions or code
"""
import unittest
import blackjack


class BlackjackTestCase(unittest.TestCase):
    """
    test cases for blackjack game functions
    """
    def test_card_value(self):
        """
        basic getter check
        :return: None
        """
        ace = blackjack.Card('Hearts', 'Ace', 11)
        self.assertEqual(ace.get_value(), 11)

    def test_deck_init(self):
        """
        checks deck is full
        :return: None
        """
        deck = blackjack.Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_deal(self):
        """
        deals few cards
        :return: None
        """
        deck = blackjack.Deck()
        hand = []
        for i in range(0, 5):
            hand.append(deck.deal())
            i += 1
        self.assertEqual(len(hand), i)
        self.assertEqual(len(deck.cards), 47)

    def test_deck_shuffle(self):
        """
        checks shuffle mixes up the cards, does not test entropy ...
        :return: None
        """
        deck1 = blackjack.Deck()
        deck2 = blackjack.Deck()
        deck1.shuffle()
        deck2.shuffle()
        hand1 = []
        hand2 = []
        for i in range(0, 50):
            hand1.append(deck1.deal())
            hand2.append(deck2.deal())
        identical = True
        for i in range(0, 50):
            if hand1[i].get_value() != hand2[i].get_value():
                identical = False
                break
        # ~ 1:30414093201713378043612608166064768844377641568960512000000000000 for false negative
        self.assertEqual(identical, False)

    def test_dealer_move(self):
        """
        makes sure Dealer hits if <=16 and stays otherwise
        :return: None
        """
        ace_card = blackjack.Card('Hearts', 'Ace', 11)
        jack_card = blackjack.Card('Clubs', 'Jack', 10)
        seven_card = blackjack.Card('Spades', 'Seven', 7)
        two_card = blackjack.Card('Diamonds', 'Two', 2)
        dealer = blackjack.Dealer('Dealer')
        dealer.hand = [ace_card, jack_card]
        self.assertEqual(dealer.play(), 's')
        dealer.hand = [ace_card, two_card]
        self.assertEqual(dealer.play(), 'h')
        dealer.hand = [ace_card, seven_card]
        self.assertEqual(dealer.play(), 's')

    def test_dealer_bet(self):
        """
        makes sure Dealer always bets 0, regardless of hand
        :return: None
        """
        ace_card = blackjack.Card('Hearts', 'Ace', 11)
        jack_card = blackjack.Card('Clubs', 'Jack', 10)
        seven_card = blackjack.Card('Spades', 'Seven', 7)
        two_card = blackjack.Card('Diamonds', 'Two', 2)
        dealer = blackjack.Dealer('Dealer')
        dealer.hand = [ace_card, jack_card]
        self.assertEqual(dealer.place_bet(), 0)
        dealer.hand = [ace_card, two_card]
        self.assertEqual(dealer.place_bet(), 0)
        dealer.hand = [ace_card, seven_card]
        self.assertEqual(dealer.place_bet(), 0)

    def test_blackjack_score(self):
        """
        check score for various cases - high, low, BUST, BLACKJACK, Ace as 1 instead of 11
        :return: None
        """
        ace_card = blackjack.Card('Hearts', 'Ace', 11)
        jack_card = blackjack.Card('Clubs', 'Jack', 10)
        nine_card = blackjack.Card('Hearts', 'Nine', 9)
        seven_card = blackjack.Card('Spades', 'Seven', 7)
        four_card = blackjack.Card('Spades', 'Four', 4)
        two_card = blackjack.Card('Diamonds', 'Two', 2)
        player = blackjack.HumanPlayer('Tester', 1000)
        player.hand = [ace_card, jack_card]
        self.assertEqual(blackjack.BlackjackGame.score(player), 21)
        player.hand = [ace_card, jack_card, nine_card]
        self.assertEqual(blackjack.BlackjackGame.score(player), 20)
        player.hand = [seven_card, jack_card, nine_card]
        self.assertEqual(blackjack.BlackjackGame.score(player), -1)
        player.hand = [seven_card, four_card]
        self.assertEqual(blackjack.BlackjackGame.score(player), 11)
        player.hand = [seven_card, four_card, nine_card]
        self.assertEqual(blackjack.BlackjackGame.score(player), 20)
        player.hand = [seven_card, four_card, two_card]
        self.assertEqual(blackjack.BlackjackGame.score(player), 13)
        player.hand = [two_card, four_card]
        self.assertEqual(blackjack.BlackjackGame.score(player), 6)


if __name__ == '__main__':
    unittest.main()
