import random
import art


def adjust_for_ace(cards):
    """Adjust Ace value from 11 to 1 if total exceeds 21."""
    while sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1
    return sum(cards)


def display_final_results(player_1_cards, total_1, player_2_cards, total_2):
    """Display the final results based on scores."""
    print(f"\nYour final hand: {player_1_cards}, final score: {total_1}")
    print(f"Computer's final hand: {player_2_cards}, final score: {total_2}")

    if total_1 > 21:
        print("You went over. You lose 😭")
    elif total_2 > 21:
        print("Opponent went over. You win 😁")
    elif total_1 > total_2:
        print("You win 😃")
    elif total_1 == total_2:
        print("Draw 🙃")
    else:
        print("You lose 😤")


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_1_cards = random.sample(cards, k=2)
    player_2_cards = random.sample(cards, k=2)

    total_1 = adjust_for_ace(player_1_cards)
    total_2 = adjust_for_ace(player_2_cards)

    print("\n" * 20)
    print(art.logo)
    print(f"Your cards: {player_1_cards}, current score: {total_1}")
    print(f"Computer's first card: {player_2_cards[0]}")

    while total_1 < 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card == "y":
            player_1_cards.append(random.choice(cards))
            total_1 = adjust_for_ace(player_1_cards)
            print(f"Your cards: {player_1_cards}, current score: {total_1}")
            print(f"Computer's first card: {player_2_cards[0]}")
        else:
            break

    display_final_results(player_1_cards, total_1, player_2_cards, total_2)


while input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower() == "y":
    blackjack()
else:
    print("Goodbye!")
