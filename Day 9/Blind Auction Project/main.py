import art
# TODO-1: Ask the user for input
print(art.logo)
print("Welcome to the secret auction program.")
# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
other_bidder = True
while other_bidder:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == "no":
        other_bidder = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 50)
        other_bidder = True
    else:
        print("Invalid input")
        other_bidder = False
        find_highest_bidder(bids)
# TODO-4: Compare bids in dictionary
