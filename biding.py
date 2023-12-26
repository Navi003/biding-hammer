 
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


def clear_console():
    print('\033c')


still_biding = True

bidders = []




print(logo)
while still_biding:
    name = input('What is your name?')
    bid = int(input('What is your bid?'))
    isThere_another_bid = input("Are ther any other biding? YES or NO").lower()
    
    bidders.append({
        "name": name,
        "bid": bid,
    })
    if isThere_another_bid == 'yes':
        clear_console()
    
    if isThere_another_bid == "no":
        max_bidder = max(bidders, key=lambda x: x["bid"]) 
        print(f"{max_bidder["name"]} highest bid of {max_bidder["bid"]} ")       
        still_biding = False
    


