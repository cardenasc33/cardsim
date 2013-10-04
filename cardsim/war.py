# -*- coding: utf-8 -*-
import random

from cardsim.deck import Deck, RANKS


class War(object):
    def __init__(self, jittery=False):
        self.jittery = jittery

        self.main_deck = Deck()
        self.main_deck.shuffle()

        self.p1, self.p2 = self.main_deck.deal([Deck(), Deck()])

        self.stats = {
            'P1': {
                'Hands won': 0,
                'Wars won': 0,
            },
            'P2': {
                'Hands won': 0,
                'Wars won': 0,
            },
            'Hands played': 0,
            'Wars played': 0,
        }

    def card_1_wins(self, card_1, card_2):
        if card_1[0] == card_2[0]:
            # They're the same.
            return None

        if RANKS.index(card_1[0]) < RANKS.index(card_2[0]):
            return False

        return True

    def player_wins(self, name, deck, cards, is_war=False):
        # Simulate a bit of random jitter.
        if self.jittery:
            random.shuffle(cards)

        for card in cards:
            deck.add_to_bottom(card)

        print("{0} takes ({1} cards - {2} total).".format(
            name,
            len(cards),
            len(deck)
        ))

        if is_war:
            self.stats[name]['Wars won'] += 1
        else:
            self.stats[name]['Hands won'] += 1

    def play_hand(self, cards=None, is_war=False):
        if cards is None:
            cards = []

        card_1 = self.p1.draw_from_top()
        card_2 = self.p2.draw_from_top()
        cards.append(card_1)
        cards.append(card_2)

        print("P1 played: ", card_1[0], card_1[1])
        print("P2 played: ", card_2[0], card_2[1])

        card_1_won = self.card_1_wins(card_1, card_2)

        if card_1_won is True:
            self.player_wins('P1', self.p1, cards, is_war=is_war)
        elif card_1_won is False:
            self.player_wins('P2', self.p2, cards, is_war=is_war)
        else:
            print("WAR!")
            self.stats['Wars played'] += 1

            if len(self.p1):
                cards.append(self.p1.draw_from_top())
            else:
                return self.player_wins('P2', self.p2, cards, is_war=True)

            if len(self.p1):
                cards.append(self.p1.draw_from_top())
            else:
                return self.player_wins('P2', self.p2, cards, is_war=True)

            if not len(self.p1):
                return self.player_wins('P2', self.p2, cards, is_war=True)

            if len(self.p2):
                cards.append(self.p2.draw_from_top())
            else:
                return self.player_wins('P1', self.p1, cards, is_war=True)

            if len(self.p2):
                cards.append(self.p2.draw_from_top())
            else:
                return self.player_wins('P1', self.p1, cards, is_war=True)

            if not len(self.p2):
                return self.player_wins('P1', self.p1, cards, is_war=True)

            print("   {0} {1} /{2} {3}  -  {4} {5} /{6} {7}".format(
                cards[-4][0],
                cards[-4][1],
                cards[-3][0],
                cards[-3][1],
                cards[-2][0],
                cards[-2][1],
                cards[-1][0],
                cards[-1][1],
            ))
            return self.play_hand(cards, is_war=True)

    def play(self):
        while len(self.p1) and len(self.p2):
            self.stats['Hands played'] += 1
            self.play_hand()
            print()

    def print_stats(self):
        if len(self.p1):
            print("PLAYER 1 WINS!")
        else:
            print("PLAYER 2 WINS!")

        print()
        print('Hands played: ', self.stats['Hands played'])
        print('Wars played:  ', self.stats['Wars played'])
        print()
        print('P1 hands won: ', self.stats['P1']['Hands won'])
        print('P1 wars won:  ', self.stats['P1']['Wars won'])
        print()
        print('P2 hands won: ', self.stats['P2']['Hands won'])
        print('P2 wars won:  ', self.stats['P2']['Wars won'])


if __name__ == '__main__':
    import sys
    jittery = False

    # Set this to compare outcomes.
    # Spoiler: With a set seed & no jitter, it plays out consistently.
    #          With a set seed & jitter, different outcomes (including a
    #          different winner!!!) happen.
    # random.seed(10)

    if len(sys.argv) == 2:
        if sys.argv[1].lower().startswith('y'):
            print("Using jitter...")
            jittery = True

    war = War(jittery=jittery)
    war.play()
    print()
    print('==========')
    print()
    print()
    war.print_stats()
