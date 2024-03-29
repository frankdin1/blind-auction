import os

# def clear():
#     print("\033[2J\033[H", end="", flush=True)


# 1. Create list that will contain dictionaries
# 2. Ask for user's name and user bid
# 3. Create function that takes user's name and bid as parameters
# Append the user bid and name to the list as a dictionary
# 4. Ask if there are other bidders
# If there are other bidders, call clear()
# 5. After the last user has put in their bid, iterate through the list and find the highest bid and his/her bidder

# 1
auction_list = [
    # {
    #     "name": "frank",
    #     "bid": 200
    # },
    # {
    #     "name": "john",
    #     "bid": 300
    # },
]


# 3
def add_to_list(user_name, user_bid):
    bid_info = {
        "name": user_name,
        "bid": user_bid,
    }
    auction_list.append(bid_info)


# 2
def get_bid_info():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    add_to_list(name, bid)


# 5
def get_highest_bid_info():
    highest_bid = auction_list[0]['bid']
    highest_bidder = auction_list[0]['name']
    for bid_num in range(len(auction_list)):
        if highest_bid < auction_list[bid_num]['bid']:
            highest_bid = auction_list[bid_num]['bid']
            highest_bidder = auction_list[bid_num]['name']
    return highest_bidder, highest_bid


# 4
def more_bidders():
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    while True:
        if other_bidders == 'yes':
            os.system('cls')
            get_bid_info()
            more_bidders()
        elif other_bidders == 'no':
            break
        break

def perform_auction():
    get_bid_info()
    more_bidders()
    highest_bid_info = get_highest_bid_info()
    print(f"The winner is {highest_bid_info[0]} with a bid of ${highest_bid_info[1]}")


perform_auction()