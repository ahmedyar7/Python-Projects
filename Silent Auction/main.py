import os
from art import logo

print(logo)


def highestBidder(biddingRecords):
    winner = ""
    highestBid = 0
    for bidders in biddingRecords:
        biddering = biddingRecords[bidders]
        if biddering > highestBid:
            highestBid = biddering
            winner = bidders

    print(f"{winner} Won!, With highest Bid of ${highestBid}")


bids = {}

bidEnd = False

while not bidEnd:
    name = input("Enter Your Name: ")
    price = int(input("Enter Your Price: "))
    bids[name] = price
    userInput = input("Do You Want to continue Yes or No: ").lower()

    if userInput == "yes":
        os.system("cls" if os.name == "nt" else "clear")
    elif userInput == "no":
        bidEnd = True
        highestBidder(bids)
    else:
        print("Please Provide Valid Input")
