def clear():
    print("\033[2J\033[H", end="", flush=True)


# 1. Create list that will contain dictionaries
# 2. Ask for user's name and user bid
# 3. Create function that takes user's name and bid as parameters
# Append the user bid and name to the list as a dictionary
# 4. Ask if there are other bidders
# If there are other bidders, call clear()
# 5. After the last user has put in their bid, iterate through the list and find the highest bid and his/her bidder

# 1
auction_list = [
    {
        "name": "frank",
        "bid": 200
    },
    {
        "name": "john",
        "bid": 300
    },
]


# 2
def get_bid_info():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    add_to_list(name, bid)


# #4
# other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
# if other_bidders == 'yes':
#   clear()
#   get_bid_info()
#
# 3
def add_to_list(user_name, user_bid):
    bid_info = {
        "name": user_name,
        "bid": user_bid,
    }
    auction_list.append(bid_info)


# #5
# def get_highest_bid():
#   highest_bid = auction_list[0]['bid']
#   highest_bidder = ""
#   for bid in auction_list:
#
# print(auction_list[0]['bid'])
# print("text")
clear()
