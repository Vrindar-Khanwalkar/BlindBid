import posix
biddict = {
    "James" : 142,
    "Kiara" : 20,
    "Emily" : 200,
}

def calhighestBidder(bid_dict):
    biggest_bid = 0
    for key in bid_dict:
        if bid_dict[key] > biggest_bid:
            biggest_bid = bid_dict[key]
            biggest_key = key
    posix.system('clear')
    print(f"The winner is {biggest_key} with a bid of ${biggest_bid}. ")


def get_bid(empty_dict):
    contBid = True

    while(contBid is True):
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))
        empty_dict[name] = bid
        bidCont = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if bidCont =='yes':
            posix.system('clear')
        else:
            contBid = False

get_bid(biddict)
calhighestBidder(bid_dict=biddict)
            


