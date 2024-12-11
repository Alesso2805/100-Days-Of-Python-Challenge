number_to_check = float(input("Enter a number: "))

remainder = round(number_to_check % 2, 2)

if remainder % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")

print(f"The remainder of the number is: {remainder}")