# Program to simulate Craps
import random

playerWins = 0
houseWins = 0

# Splash screen
# Not my own ASCII Art - sourced from
# https://www.asciiart.eu/miscellaneous/dice
print("------- CRAPS SIMULATOR 9000 -------")
print("""
          ____
         /\\' .\\    _____
        /: \\___\\  / .  /\\
        \\' / . / /____/..\\
         \\/___/  \\'  '\\  /
                  \\'__'\\/

------------------------------------
""")

# player rolls 2 dice
def roll():
    roll = random.randint(1,6)+random.randint(1,6)
    return roll

# end the game (1=player win, 0=house win)
def endGame(r):
    global playerWins
    global houseWins
    if r==1: playerWins+=1
    if r==0: houseWins+=1

# start game
def newGame():
    roll1 = roll()
    if(roll1==11 or roll1==7): #win & gameover
        endGame(1)
    elif(roll1==2 or roll1==3 or roll1==12): #lose & gameover
        endGame(0)
    else: #loop until player gets roll1 or 7
        tempSum = roll1
        rollq = 0
        rolling=True
        while(rolling):
            rollq=roll()
            if(rollq==tempSum): #win & gameover
                rolling=False
                endGame(1)
            elif(rollq==7): #lose & gameover
                rolling=False
                endGame(0)

# perform user specified # of games
numGames = 0
while True:
    try:
        numGames = int(input("How many games would you like to play? "))
        break
    except KeyboardInterrupt:
        exit()
    except:
        print("Input only a number value!")

for i in range(0,numGames):
    newGame()

print(f"Player Wins: {playerWins}")
print(f"House Wins: {houseWins}")

percP = (playerWins/numGames)*100
percH = (houseWins/numGames)*100
print(f"Probability of player winning: {percP:.2f}%")
print(f"Probability of house winning: {percH:.2f}%")
