import random

suits = {}.fromkeys(['Spades','Clubs','Hearts','Diamonds'],0)
cardVals = {}

def fillDict():
    # Fill the dictionary with all possible cards
    for x in suits:
        cardVals.update(dict.fromkeys([f'Jack of {x}',f'King of {x}',f'Queen of {x}'],10))
        cardVals.update({f'{y} of {x}': y for y in range(2,11)})
        cardVals.update({f'Ace of {x}':1})

def pickCard():
    # Pick a random card from the selection
    randVal = random.choice(list(cardVals.keys()))
    if('Ace' in randVal):
        while True:
            try:
                process = int(input("You got an Ace! What value would you like? (1 or 11): "))
                if(process==1 or process==11):
                    cardVals[randVal]=process
                    break
                else:
                    print("Enter only 1 or 11")
                    continue
            except KeyboardInterrupt:
                print("Goodbye.")
                exit()
            except:
                print("Enter only 1 or 11")
    # Get & return card & remove it
    val = cardVals[randVal]
    cardVals.pop(randVal)
    return randVal, val

# Main loop
fillDict()
print(f"""------------------------------------
Displaying Deck Before Loop
------------------------------------
{cardVals.keys()}
------------------------------------
""")
running = True
while running:
    process = 0
    while True:
        try:
            process = int(input("How many cards should I deal? "))
            if(process>0 & process<53):
                break
        except KeyboardInterrupt:
            print("Goodbye.")
            exit()
        except:
            print("Enter only a numerical value.")


    handValue = 0
    # Pull X # of cards.
    for x in range(process):
        tmpCall = pickCard()
        tmpCard = tmpCall[0] # Get card name
        tmpVal = tmpCall[1] # Get card value
        handValue += tmpVal
        print(tmpCard)
    print(f"Value of this hand: {handValue}")
