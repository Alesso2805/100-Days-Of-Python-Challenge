import random
import art
import game_data

print(art.logo)


def randomize_player():
    player_name_a = random.choice(game_data.data)
    player_name_b = random.choice(game_data.data)

    while player_name_a == player_name_b:
        player_name_b = random.choice(game_data.data)

    return player_name_a, player_name_b


def print_comparison(player_a, player_b):
    print(f"Compare A: {player_a['name']}, a {player_a['description']}, from {player_a['country']}")
    print(art.vs)
    print(f"Compare B: {player_b['name']}, a {player_b['description']}, from {player_b['country']}")


def make_choice(player_a, player_b):
    """Handles user input and checks if the choice is correct."""
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if answer == 'a' and player_a['follower_count'] > player_b['follower_count']:
        return True
    elif answer == 'b' and player_b['follower_count'] > player_a['follower_count']:
        return True
    else:
        return False


score = 0
player_a, player_b = randomize_player()

while True:
    print_comparison(player_a, player_b)

    if make_choice(player_a, player_b):
        score += 1
        print(f"You're right! Current score: {score}")

        # Randomize new players, keeping player B as the next player A
        player_a = player_b
        player_b = random.choice(game_data.data)

        # Ensure player A and player B are not the same
        while player_a == player_b:
            player_b = random.choice(game_data.data)
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        break
