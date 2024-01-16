# Python Blackjack

#### [Video Demo](https://youtu.be/-HghMVU3iVQ)

#### Description:

This is my final project for CS50P. Recreation of undying classic of casino games, made with Python and playable through command line.

There is no need for installation. Simply put all files to directory and change to this directory in command line. Command `python project.py` will start the game.

**How to Play**
The main goal of the game is to get a hand value as close to 21 as possible without going higher (busting). If player gets exactly 21, it's called a Blackjack and it is an automatic win. Also, if player gets 21 on the initial deal, it's called "Natural" and bet is multiplied by 1.5. Player competes against the dealer, who also can get Blackjack or get busted. But if no one at the end of the game has 21 or more, the game will count who has the highest and closest to 21 hand values, with the highest guarantees winning. Also, there is no ties, so if player and dealer both have the same value, player wins. Player places bets every round of blackjack - winning returns the bet and adds corresponding amount to player's wallet, failure detracts the bet's value from the wallet.

After game starts, it will ask player `Shall we play a game? (y/n)`. Affirmative answer - `y`, will begin the first round. Negative `n` will exit the programme.

The first thing player will see is a wallet with default value 100 - `Your current score: 100`. The game offers player to place a bet: `Place your bet (a number and at least 10): ` The game will check if the bet is correct - at least 10, but not higher, then player have in their a wallet. When the bet is placed, the game will again inform player how much he bet - `Your bet is: 10`.

When all monetary considerations are done, the initial deal will commit. The game will inform player about cards of both them and the dealer, and also count the hand value of former. While dealer has only two cards in hand, the second one will be hidden from player to keep the intrigue and strategy to the game. Second card will be reveled at the end of the game or if dealer draws more cards.
```
Dealer current cards: 3♢, [Hidden]
Your current cards: Q♤, 4♡        
Your hand value: 14
--------------------
```

After presenting the information, the game then asks player to decide what they want to do next - `Hit or stand?`. Hit (`h` or `hit`) means to draw a card and stand (`s` or `stand`) means that the dealer will draw cards. If player chooses first option, `h` or `hit`, they will draw one card, information will be updated correspondingly and the choice to hit or stand will be presented again, if conditions for blackjack or getting busted are not met. If player chooses second option, `s` or `stand`, the dealer will draw cards until it has a total hand value of 17 or higher. If no one has hand value of 21 or higher,the game will calculate who got closer to the desired number. In the case of tie, when both player and dealer has equal hand value, the player will win the game.

When rounds ends and scores are calculated, the console will clear and final status message will be presented to the player. It contains information on how much player won or lost, how much money is left in the wallet, cards in hand of player and dealer and their hand values.
```
You win 10 and you current wallet is 110
Your current cards: Q♤, 4♡, 6♤
Dealer current cards: 3♢, 2♢, 2♤, K♢
Player final score: 20 Dealer final score: 17
--------------------
```

Afterwards, the game will again ask `Shall we play a game? (y/n)`. While player continues to play, the wallet value will carry over for subsequent plays. If there is not enough money in the wallet to place a bet (less then 10), the game will display the message `You are out of money, sorry! Restart the game` and asks player `Restart the game? (y/n)`. Affirmative answer will reset wallet value to default 100 and the game will begin again.