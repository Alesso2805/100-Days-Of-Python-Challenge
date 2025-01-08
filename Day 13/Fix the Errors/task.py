try:
    age = int(input("How old are you?"))
except ValueError:
    print("Please enter a valid number such as 10, 11, 12, etc.")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
elif age < 18:
    print(f"You can't drive at age {age}.")
