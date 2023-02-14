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

print(rollDice(5,8))