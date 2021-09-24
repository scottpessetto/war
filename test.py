from war import war_deck

deck = war_deck(1)
deck.create_deck()
print(deck.deck)

deck.shuffle_deck()

print(deck.deck)

deck.split_deck()

print(deck.p1)
print(deck.p2)
