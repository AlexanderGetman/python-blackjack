import random
import os
from classes.players import Human, Dealer

def main():
    global separator
    separator = "--------------------\n"
    ask_for_a_game()
    
    deck = generate_deck()
    #Statement here checks for variable 'wallet' in global variables - if there is any, it's value is stored in player's wallet. If not, it sets wallet to default 100
    player = Human(wallet = wallet if "wallet" in globals() else 100)
    dealer = Dealer()
    check_wallet(player, dealer)
    initial_deal(deck, player, dealer)
    play_round(deck, player, dealer)

def ask_for_a_game():
    while True:
        print(separator)
        play_game = input("Shall we play a game? (y/n) ")
        if play_game == 'y':
            break
        elif play_game == 'n':
            print('Thank you for playing!')
            exit()

#Generates a complete and shuffled deck of 52 cards
def generate_deck():
    suits = ["♡","♤","♧","♢"]
    numbers = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    deck = []
    for suit in suits:
        for number in numbers:
            deck.append(number + suit)
    random.shuffle(deck)
    return deck

#Initial deal at the start of the game - two cards for both player and dealer
def initial_deal(deck, player, dealer): 
    player.hand.append(deck.pop())
    dealer.hand.append(deck.pop())
    player.hand.append(deck.pop())
    dealer.hand.append(deck.pop())

#This function plays a round of blackjack - it displays current cards and hand value and asks player to decide to hit or to stand
#After player and/or dealer do their moves, it calls function 'check_scores()'
def play_round(deck, player, dealer):
    print(dealer)
    print(player)
    check_scores(player, dealer)
    print("Your hand value: " + str(player.value()))
    print(separator)

    choice = input('Hit or stand? ')
    print(separator)
    if choice.lower() == 'hit' or choice.lower() == 'h':
        player.hand.append(deck.pop())
        play_round(deck, player, dealer)
    if choice.lower() == 'stand' or choice.lower() == 's':
        while dealer.value() < 17:
            dealer.hand.append(deck.pop())
        check_scores(player, dealer, "game commenced")
    while choice.lower() not in ['hit', 'h', 'stand', 's']:
        print('Invalid choice. Please enter "hit", "h" or "stand", "s".')
        play_round(deck, player, dealer)

#Checks player wallet if it has enough money to continue the game. If there is enough money, it calls Human.place_bet() method to make a bet. If not, it suggests player to reset the game and try once more
def check_wallet(player, dealer):
    print(player.score())
    if player.wallet < 10:
        print("You are out of money, sorry! Restart the game")
        while True:
            restart = input("Restart the game? (y/n) ")
            if restart == "y":
                reset(player, dealer)
                global wallet
                wallet = 100
                main()
            elif restart == "n":
                print("Thank you for playing!")
                exit()
    player.place_bet()


#Checks current scores of the players and depending on the score calls 'display_results()' function.
#As third argument takes 'condition' variable. Default 'game in progress' means that there is left options for other moves by player, 'game commenced' - there is no moves left and scores can be compared.
def check_scores(player, dealer, condition="game in progress"):
    if player.value() == 21 and len(player.hand) == 2:
        display_results(player, dealer, 'natural')
    elif player.value() == 21:
        display_results(player, dealer, 'blackjack')
    elif player.value() > 21:
        display_results(player, dealer, 'bust')
    elif dealer.value() > 21:
        display_results(player, dealer, 'dealer-bust')
    elif dealer.value() == 21:
        display_results(player, dealer, 'dealer-blackjack')
    
    if condition == "game commenced":
        if player.value() >= dealer.value():
            display_results(player, dealer, 'win')
        elif player.value() < dealer.value():
            display_results(player, dealer, 'lost')

#Resets both player and dealer variables to it's initial state
def reset(player, dealer):
    player.reset()
    dealer.reset()

#This one displays results of the game depending on the winning or loosing condition and makes corresponding arithmetic operations with the wallet
def display_results(player, dealer, condition):

    #This functions, that is using 'os' lib, simply clears the console to display results more clear and visually compelling
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')

    #This nested function displays results in the end of the game, stores player wallet value to the global variable and then restarts the game
    def display_scores(player, dealer):
        dealer.hidden = False
        print(player)
        print(dealer)
        print("Player final score: " +  str(player.value()) + " Dealer final score: " +  str(dealer.value()))
        reset(player, dealer)
        global wallet 
        wallet = player.wallet
        main()
    
    match condition:
        case "natural":
            cls()
            print('Blackjack! Natural!')
            player.wallet += int(player.bet * 1.5)
            print('You win ' + str(int(player.bet * 1.5)) + ' and you current wallet is ' + str(player.wallet))
            display_scores(player, dealer)
        case "win":
            cls()
            player.wallet += int(player.bet)
            print('You win ' + str(player.bet) + ' and you current wallet is ' + str(player.wallet))
            display_scores(player, dealer)
        case "lost":
            cls()
            player.wallet -= int(player.bet)
            print('You loose ' + str(player.bet) + ' and you current wallet is ' + str(player.wallet))
            display_scores(player, dealer)
        case "blackjack":
            cls()
            print("You've got Blackjack!")
            player.wallet += int(player.bet)
            print('You win ' + str(player.bet) + ' and you current wallet is ' + str(player.wallet))
            display_scores(player, dealer)
        case "dealer-blackjack":
            cls()
            print("Dealer got Blackjack!")
            player.wallet -= int(player.bet)
            print('You loose ' + str(player.bet) + ' and you current wallet is ' + str(player.wallet))
            display_scores(player, dealer)
        case "bust":
            cls()
            print("Bust!")
            player.wallet -= int(player.bet)
            print('You loose ' + str(player.bet) + ' and you current wallet is ' + str(player.wallet))
            display_scores(player, dealer)
        case "dealer-bust":
            cls()
            print("Dealer bust!")
            player.wallet += int(player.bet)
            print('You win ' + str(player.bet) + ' and you current wallet is ' + str(player.wallet))
            display_scores(player, dealer)

if __name__ == "__main__":
    main()