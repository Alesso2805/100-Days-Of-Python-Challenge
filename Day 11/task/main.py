import random

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

elements_to_pick = random.randint(2, 3)



player_cards = []

confirmation = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()

if confirmation == 'y':
    print(art.logo)
    for picked_cards in range(elements_to_pick):
        random_element = random.choice(cards)
        player_cards.append(random_element)
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
else:
    print("Goodbye!")