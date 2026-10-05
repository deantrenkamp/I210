import random

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

suits = ["♣", "♦", "♥", "♠"]

card_deck = []

for rank in ranks:
    for suit in suits:
        card_deck.append(rank + suit)
        random.shuffle(card_deck)

print(card_deck)

players = int(input("How many players are there (1-5)? "))

if (players < 1) or (players > 5):
    print("You may only choose numbers between 1 and 5.")
    players = int(input("How many players are there (1-5)? "))

player_hands = []

for i in range (players):
    hand = []
    for i in range(5):
        hand.append(card_deck.pop())
    player_hands.append(hand)

for i in range(len(player_hands)):
    print(f"Player {i+1}'s hand: {player_hands[i]}")
 




