# -*- coding: utf-8 -*-
import random

RANKS = [
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'J',
    'Q',
    'K',
    'A',
]
SUITS = [
    '♤',
    '♧',
    '♡',
    '♢',
]


class Deck(object):
    def __init__(self):
        self.cards = []

    def __iter__(self):
        return iter(self.cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def shuffle(self):
        self.cards = []

        for rank in RANKS:
            for suit in SUITS:
                self.cards.append((rank, suit))

        random.shuffle(self.cards)

    def deal(self, decks):
        deck_count = len(decks)

        for offset, card_tuple in enumerate(self.cards):
            deck_choice = offset % deck_count
            decks[deck_choice].add_to_top(card_tuple)

        return decks

    def add_to_top(self, card_tuple):
        self.cards.insert(0, card_tuple)

    def add_to_bottom(self, card_tuple):
        self.cards.append(card_tuple)

    def draw_from_top(self):
        return self.cards.pop(0)
