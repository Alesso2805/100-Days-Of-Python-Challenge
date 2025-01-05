import random

import art

print(art.logo + "\nWelcome to the Number Guessing Game!" + "\nI'm thinking of a number between 1 and 100.")

def guess_number():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        guess_number()

    number = random.randint(1, 100)

    while attempts > 0:
        print(f"You have {attempts} attempts   remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > 100 or guess < 1:
            print("Please enter a number between 1 and 100.")
        elif guess > number:
            print("Too high.")
            print("Guess again.")
            attempts -= 1
        elif guess < number:
            print("Too low.")
            print("Guess again.")
            attempts -= 1
        else:
            print(f"You got it! The answer was {number}.")
            break
    if attempts == 0:
        print(f"You've run out of guesses, you lose. The number was {number}.")

guess_number()
while input("Do you want to play again? Type 'yes' or 'no': ").lower() == "yes":
    guess_number()
print("Goodbye!")