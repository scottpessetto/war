import pandas as pd
import numpy as np
import random

class war_deck:
    def __init__(self, seed):
       self.seed=seed
    
    def create_deck(self):
       self.deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] * 4

    def shuffle_deck(self):
        #self.deck = random.shuffle(self.deck)
        self.deck=(random.sample(self.deck,len(self.deck)))

    def split_deck(self):
        self.p1 = self.deck[:len(self.deck)//2]
        self.p2 = self.deck[len(self.deck)//2:]

    def simulate(self):
        if (len(p1)>0) && (len(p2)>0):
            p1_card = p1.pop()
            p2_card = p2.pop()
        elif:
            print('Game over')