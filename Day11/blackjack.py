import random


draw_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


cards_draw = True
while cards_draw:

    computer_cards = list()

    # Get two random cards
    def card_drawn(draw_cards):
        cards = list()
        card_count = 0
        for i in draw_cards:
            cards.append(draw_cards[random.randint(0,12)])
            card_count += 1
            if card_count == 2:
                break
        return cards


    def draw_single_card(draw_cards,cards):
        card_count = 0
        for i in draw_cards:
            cards.append(draw_cards[random.randint(0,12)])
            card_count += 1
            if card_count == 1:
                break
        return cards

    user_cards = card_drawn(draw_cards)
    print(f"User cards: {user_cards}")
    computer_cards = card_drawn(draw_cards)
    print(f"Computer card: {computer_cards[0]}")

    # Add up the random cards
    def sum_list(list_item):
        sum_items = 0
        for j in list_item:
            sum_items = sum_items +j
        return sum_items

    total_cards_user = sum_list(user_cards)
    print(total_cards_user)
    total_cards_computer = sum_list(computer_cards)
    print(total_cards_computer)

    #Check blackjack
    def check_blackjack(check,user):
        if check == 21:
            print(f"{user} has blackjack. {user} Win")

    check_blackjack(total_cards_user,"User")
    check_blackjack(total_cards_computer,"Computer")

    def score_over(check_list,over21):
        def check_over_21(over21):
            count = 0
            if over21 > 21:
                for i in check_list:
                    if i == 11:
                        check_list[count] = 1
                        over21 = sum_list(check_list)
                        check_over_21(over21)
                
                    else:
                        print("Lose")
                        cards_draw = False
                        exit(0)
            else:
                
                draw_user_next_card = input("Do you want to draw card? 'y' or 'n': ")
                if draw_user_next_card == 'y':
                    next_card = draw_single_card(draw_cards,user_cards)
                    print(next_card)
                    sum_of_next_card = sum_list(next_card)
                    print(f"User sum: {sum_of_next_card}")
                    check_over_21(sum_of_next_card)
                    
                if draw_user_next_card == "n":
                    computer_next_card = draw_single_card(draw_cards, computer_cards)
                    print(computer_next_card)
                    sum_computer_next_card = sum_list(computer_next_card)
                    print(f"Computer sum: {sum_computer_next_card}")
                    if sum_computer_next_card > total_cards_user and sum_computer_next_card <= 21:
                        print(f"Computer wins with {sum_computer_next_card} cards and user with {total_cards_user}")
                        exit(0)
                    else:

                        check_over_21(sum_computer_next_card)

                

        check_over_21(over21)  
    score_over(user_cards, total_cards_user)

