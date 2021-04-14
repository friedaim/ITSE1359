from random import randint as rand
import math

#create list
size = 200
l = [rand(55,99) for x in range(size)]

def sortList():
    #sort list in ascending
    l.sort()
    print(l)


def listScores():
    sepSize = 10
    tmpCount=0
    for x in range(int(size/sepSize)):
        newL = l[sepSize*tmpCount:sepSize*(tmpCount+1)]
        print(newL)
        tmpCount+=1

def calcMean():
    avg = 0
    for x in l:
        avg+=x
    avg=avg/len(l)
    return avg

def calcVar(avg):
    vari = 0
    for x in l:
        vari+= ((avg-x)**2)
    vari = vari/len(l)
    vari = math.sqrt(vari)
    return(vari)

def calcMed():
    med = 0
    if(len(l)%2==0):
        # # of items in list is even
        med = l[int(len(l)/2)]
    else:
        # # of items in list is odd
        med = l[round(len(l)/2)]
    return med

print("Full sorted list...")
sortList()
print("Separated 10-item lists...")
listScores()
avg = calcMean()
print(f"The Average is {avg}")
vari = calcVar(avg)
print(f"The Variance is {vari:.3f}")
med = calcMed()
print(f"The median value is {med}")
