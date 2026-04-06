from art import logo

print(logo)
bidding = True
bid_dictionary = {}

while bidding:
    highest_bid = 0
    name = input("What is your name? ")
    bid = float(input("How much are you bidding? $"))
    bid_dictionary[name] = bid
    other_bidders = input("Are there any other bidders? Type yes or no ").lower()

    if other_bidders == "yes":
        print("\n" * 100)

    else:
        for bid in bid_dictionary:
            if bid_dictionary[bid] > highest_bid:
                highest_bid = bid_dictionary[bid]
        print(f"The winner is {bid} with a bid of ${highest_bid}")
        bidding = False

