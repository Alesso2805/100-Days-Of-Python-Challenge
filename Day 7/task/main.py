import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
while "_" in placeholder:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            placeholder = list(placeholder)
            placeholder[position] = letter
            placeholder = "".join(placeholder)
    print(placeholder)

display = ""

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
