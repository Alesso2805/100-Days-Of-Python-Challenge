enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


def drink_potion():
    potion_strength = 2
    print(potion_strength)

potion_strength = 3
drink_potion()
print(potion_strength)

####################################

def game():
    def drink_potion():
        potion_strength = 2
        print(potion_strength)

    drink_potion()

game()



