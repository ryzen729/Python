import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
ask_price = True
bidding = {}
max_bid = list()
while ask_price:
    #Enter name
    name = input("Enter your name: ")
    price = int(input("Enter the bid price: "))
    bidding[name] = price
    bid_continue = input("Are there any more bidders? Type 'yes' or 'no'. ")
    if bid_continue == "yes":
        os.system('clear')
    else:
        #Find max bid
        for keys in bidding:
            max_bid.append(bidding[keys])
        max_value = max(max_bid)
        for k,v in bidding.items():
            if v == max_value:
                name = k
        #print(bidding)
        print(f"The winner is {name} with a bid of ${max_value}")
        ask_price = False



            


