import random

numbers = []
for item in range(13):
    numbers.append(item + 1)

listofnumbers = []

for count in range(4):
    for item in numbers:
        listofnumbers.append(item)

suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
deck = {}
for suit in suits:
    for number in numbers:
        form = ""
        if number == 1:
            form = "Ace"
        elif number == 11:
            form = "Jack"
        elif number == 12:
            form = "Queen"
        elif number == 13:
            form = "King"
        else:
            form = str(number)
        cur = form + " of " + suit;
        if number > 9:
            number = 10
        deck[cur] = number;

soledeck = []
dealerNumber = 0
playerNumber = 0
answer = ""
player_hand = ""
dealer_hand = ""
game_over = False

for keys in deck:
    soledeck.append(keys)

if dealerNumber < 17:
    dealerCard = soledeck.pop(random.randint(0, len(soledeck) - 1))
    dealer_hand += dealerCard + "; "
    dealerNumber += deck.pop(dealerCard)
print("Dealer: " + dealer_hand + ": " + str(dealerNumber))

for _ in range(2):
    playerCard = soledeck.pop(random.randint(0, len(soledeck) - 1))
    if playerCard[0:3] == "Ace":
        playerNumber += int(input("You drew an Ace. Do you choose 1 or 11: "))
        deck.pop(playerCard)
    else:
        playerNumber += deck.pop(playerCard)
    player_hand += playerCard + "; "
print("You: " + player_hand + ": " + str(playerNumber))
print()

if dealerNumber == 21:
    print('You Lose')
    game_over = True

if playerNumber == 21:
    print('You Win')
    game_over = True

answer = input("Hit or Stop: ").lower()

while answer != "stop" and not game_over:

    playerCard = soledeck.pop(random.randint(0, len(soledeck) - 1))
    if playerCard[0:3] == "Ace":
        playerNumber += int(input("You drew an Ace. Do you choose 1 or 11: "))
        deck.pop(playerCard)
    else:
        playerNumber += deck.pop(playerCard)
    player_hand += playerCard + "; "
    print("You: " + player_hand + ": " + str(playerNumber))
    print()

    if dealerNumber == 21:
        print('You Lose')
        game_over = True
        break

    if playerNumber == 21:
        print('You Win')
        game_over = True
        break

    if playerNumber > 21:
        print('You Busted')
        game_over = True
        break

    if answer != "stop":
        answer = input("Hit or Stop: ").lower()

if not game_over:
    while dealerNumber < 5:
        dealerCard = soledeck.pop(random.randint(0, len(soledeck) - 1))
        dealer_hand += dealerCard + "; "
        dealerNumber += deck.pop(dealerCard)
    print("Dealer: " + dealer_hand + ": " + str(dealerNumber))

    if dealerNumber > 21:
        print("You Win")
    else:
        if playerNumber < 21:
            if playerNumber > dealerNumber:
                print("You Win")
            elif playerNumber < dealerNumber:
                print("You Lose")
            else:
                print("You tied with the dealer")