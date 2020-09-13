def average(list):

    #gets the number of items in the list
    numOfItems = len(list)

    #averages the list
    averagingTheNum = sum(list) / numOfItems

    #prints the average
    print(averagingTheNum)

def diceRoll(num):
    import random

    sidesOfDice = random.randint(0, num)

    print(sidesOfDice)