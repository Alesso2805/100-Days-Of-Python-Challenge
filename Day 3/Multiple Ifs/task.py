print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(f"Children tickets are ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}.")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3
        print(f"Photo costs ${bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")
