# make 2-player blackjack game with AI incorporated
import random

suits = {}.fromkeys(['Spades','Clubs','Hearts','Diamonds'],0)
cardVals = {}

def fillDict():
    # Fill the dictionary with all possible cards
    for x in suits:
        cardVals.update(dict.fromkeys([f'Jack of {x}',f'King of {x}',f'Queen of {x}'],10))
        cardVals.update({f'{y} of {x}': y for y in range(2,11)})
        cardVals.update({f'Ace of {x}':11})

def pickCard(cardArr):
    # Pick a random card from the selection
    randVal = random.choice(list(cardArr.keys()))
    # Get & return card & remove it
    val = cardArr[randVal]
    cardArr.pop(randVal)
    return randVal, val

# Main loop
while True:
    try:
        cont = input("Play a game? (Y/N) ")
        if(cont == "N" or cont == 'n'):
            break
    except KeyboardInterrupt:
        exit()
    fillDict()
    handValueA = 0
    handValueB = 0
    # All of above pulled form PSET12 PGM1.py
    # Everything below altered for PSET13
    cardValsA = {}
    cardValsB = {}
    winner = False
    while handValueA<=21 or handValueB<=21 or (not winner):
        # Player 1
        tmpCall = pickCard(cardVals)
        tmpDict = {tmpCall[0]:tmpCall[1]}
        cardValsA.update(tmpDict)
        cardName = tmpCall[0]
        handValueA += tmpCall[1]
        if('Ace' in cardName and handValueA>21):
            cardValsA.pop(tmpCall[0])
            cardValsA.update({tmpCall[0]:1})
            handValueA-= tmpCall[1]
            handValueA+= 1
            print(f"Player 1 was dealt {cardName}")
            print("Player 1 now has >21, changing Ace value to 1...")
        else:
            print(f"Player 1 was dealt {cardName}")
        # Player 2
        tmpCall = pickCard(cardVals)
        tmpDict = {tmpCall[0]:tmpCall[1]}
        cardValsB.update(tmpDict)
        cardName = tmpCall[0] # Get card name
        handValueB += tmpCall[1]
        if('Ace' in cardName and handValueB>21):
            cardValsB.pop(tmpCall[0])
            cardValsB.update({tmpCall[0]:1})
            handValueB-= tmpCall[1]
            handValueB+= 1
            print(f"Player 2 was dealt {cardName}")
            print("Player 2 now has >21, changing Ace value to 1...\n")
        else:
            print(f"Player 2 was dealt {cardName}\n")
        if(handValueA==21 or (handValueB>21 and handValueA<21)):
            print("Player 1 wins")
            winner=True
            break
        if(handValueB==21 or (handValueA>21 and handValueB<21)):
            print("Player 2 wins")
            winner=True
            break
        if(handValueA>21 and handValueB>21 or (handValueA==21 and handValueB==21)):
            print("No one wins!")
            winner=True
            break
        
