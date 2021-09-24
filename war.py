import pandas as pd
import numpy as np
import random


class war_deck:
    def __init__(self, seed):
        self.seed = seed

    def create_deck(self):
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

    def shuffle_deck(self):
        # self.deck = random.shuffle(self.deck)
        self.deck = random.sample(self.deck, len(self.deck))

    def split_deck(self):
        self.p1 = self.deck[: len(self.deck) // 2]
        self.p2 = self.deck[len(self.deck) // 2 :]

    def draw(self):
        if (len(self.p1) > 0) & (len(self.p2) > 0):
            self.p1_card = self.p1.pop()
            self.p2_card = self.p2.pop()
            if self.p1_card > self.p2_card:
                self.p1.insert(0, self.p2_card)
                self.p1.insert(0, self.p1_card)

            elif self.p1_card == self.p2_card:
                print("tie")
            else:
                self.p2.insert(0, self.p1_card)
                self.p2.insert(0, self.p1_card)
        else:
            print("Game over")
            print(self.p1.len())
            print(self.p2.len())
