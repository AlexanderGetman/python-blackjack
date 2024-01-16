import re

class Player:
    def __init__(self, hand=[]):
        self.hand = hand

    #Calculates current hand value
    def hand_value(self):
        value = 0
        for card in self.hand:
            value += int(re.findall(r'\d+', card)[0]) if any(char.isdigit() for char in card) else 0
            if any(number in card for number in ["J", "K", "Q"]):
                value += 10
            elif "A" in card:
                value += 1 if value > 10 else 11
        return value

class Human(Player):
    def __init__(self, wallet, bet=0, hand=[]):
        self.wallet = wallet
        self.reset()

    def value(self):
        value = super(Human, self).hand_value()
        return value

    def score(self):
        return f"Your current score: {self.wallet}"
    
    #This method is used for betting - it asks player for the bet not lower then 10 and not higher, then left money in the wallet
    #It stores bet in the 'bet' variable
    def place_bet(self):
        while True:
            self.bet = input("Place your bet (a number and at least 10): ")
            if self.bet.isdigit():
                self.bet = int(self.bet)
                if self.bet >=10 and self.bet <= self.wallet:                    
                    break
        print("Your bet is: " + str(self.bet) + "\n")
        return self.bet
    
    #This method resets the state of the player in the end of the game
    def reset(self):
        self.bet = 0
        self.hand = []

    def __str__(self):
        return f"Your current cards: {', '.join(self.hand)}"

class Dealer(Player):
    def __init__(self, hand=[], hidden=True):
        self.reset()
    
    def value(self):
        value = super(Dealer, self).hand_value()
        return value

    #This one checks for conditions to show or to hide second card after the initial deal
    def check_hidden(self):
        if len(self.hand) > 2 or self.value() == 21:
            self.hidden = False
    
    #This method resets the state of the dealer in the end of the game
    def reset(self):
        self.hand = []
        self.hidden = True

    #String method here first checks for the state of 'hidden' variable, and depending on it then prints information about the cards in hand
    def __str__(self):
        self.check_hidden()
        if self.hidden:
            return f"Dealer current cards: {self.hand[0] + ', [Hidden]'}"
        else:
            return f"Dealer current cards: {', '.join(self.hand)}"