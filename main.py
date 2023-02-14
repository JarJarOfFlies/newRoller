import random

def rollDice(rolls=1, sides=6, startZero=False):
    begin=1
    end=sides
    rollList=[]
    if startZero:
        begin=0
    for i in range(rolls):
        rollList.append(random.randrange(begin,end))
    return rollList

def rollAdvantage(sides=20):
    return max(rollDice(2, sides))

def rollDisadvantage(sides=20):
    return min(rollDice(2, sides))

print(rollDisadvantage(20))