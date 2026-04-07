import random
from art import logo

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if start_game == "n":
    quit()



while start_game == "y":
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []



    # add 2 cards to the computer and user's initial decks
    for i in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))


    # if user or player has greater than 21, the ace is 1 point
    if sum(computer_cards) > 21 and 11 in computer_cards:
        computer_cards[computer_cards.index(11)] = 1

    if sum(user_cards) > 21 and 11 in user_cards:
        user_cards[user_cards.index(11)] = 1


    #Print user's current cards and computer's first card
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")


    #Check who won
    def check_winner(computer,user):
        if sum(computer) == 21:
            return "You lose! Opponent has 21"
        elif sum(user) == sum(computer):
            return "It's a draw"
        elif sum(computer) > 21:
            return "You win! Opponent went over!"
        elif sum(user) == 21:
            return "You win! You have 21"
        elif sum(computer) > sum(user):
            return "You lose! Opponent is closer to 21"
        elif sum(user) > 21:
            return "You lose! You went over 21"



    draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    # let user keep drawing until they go over 21
    while draw_card == "y":
        user_cards.append(random.choice(cards))
        print(f"Your cards: {user_cards} ")
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if sum(user_cards) > 21:
            break

    #While computer has less than 16, let it pick
    while sum(computer_cards) < 16:
        computer_cards.append(random.choice(cards))

    print(f"Your final hand {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

    print(check_winner(computer_cards, user_cards))

    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
