# Game to make user guess number
import random

answer = 0
loop = True
displayMSG = ""

# Function for easier access to guesses.
def getGuess():
    while True:
        try:
            guessIn = int(input(displayMSG))
            break
        except KeyboardInterrupt:
            exit()
        except:
            print("Nice try, enter only a numberic value!")
    return guessIn

# Game loop
print("Guess the number I've created between 0 and 100.")
while loop:
    print("""\n********* BEGIN A GAME *********\n""")
    displayMSG = ("I'm thinking of anumber. Can you"+
    " guess what it is? ")
    answer = random.randint(0,100)
    guess = 0
    guesses = 0
    while loop:
        guess = getGuess()
        guesses+=1
        if(guess<answer):
            print("Too low, try again.")
            displayMSG = "Guess again: "
        if(guess>answer):
            print("Too high, try again.")
            displayMSG = "Guess again: "
        if(guess==answer):
            print("Congratulations! You guessed it!"
            f" I was thinking of the number {answer}.")
            print(f"You got it right in {guesses} guesses.")
            print("""\n********* END OF A GAME *********\n""")
            while True:
                try:
                    read = input("Would you like to play "+
                    "another game? ('y' or 'n'):")
                except KeyboardInterrupt:
                    exit()
                if(read=='y'):
                    loop = True
                    break
                elif(read=='n'):
                    loop = False
                    print("GG")
                    break
                elif(read==KeyboardInterrupt):
                    exit()
                else:
                    print("Input not recognized.")
            break
