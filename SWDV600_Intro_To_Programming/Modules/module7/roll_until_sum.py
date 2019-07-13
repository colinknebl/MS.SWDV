# roll_until_sum.py
#
# A program that simulates rolling two 6-sided dice,
#  and repeatedly rolls them until a target sum is reached.

from random import randrange

class Dice:
    def __init__(self):
        self._dieValues = [0, 0]
    
    def roll(self):
        newValues = []
        for value in range(2):
            newValues.append(randrange(1, 7))
        self._dieValues = newValues
        
    def getValues(self):
        return self._dieValues[0], self._dieValues[1]
        
    def getTotal(self):
        return self._dieValues[0] + self._dieValues[1]
    

def printRollResults(dice):
    die1Val, die2Val = dice.getValues()
    print('Roll: {} and {}, sum is {}'.format(die1Val, die2Val, dice.getTotal()))

def startRolling(targetVal):
    dice = Dice()
    dice.roll()
    rollVal = dice.getTotal()
    numOfRolls = 1
    printRollResults(dice)
    
    while rollVal != targetVal:
        dice.roll()
        numOfRolls += 1
        printRollResults(dice)
        rollVal = dice.getTotal()
    
    return numOfRolls

def getTargetVal():
    targetVal = int(input('Enter the target sum to roll for: '))
    print()
    
    while targetVal < 2 or targetVal > 12:
        targetVal = int(input('Out of range, please enter a number between 2 and 12: '))
    return targetVal

def main():
    print('This program rolls two 6-sided dice until their sum is a given target value.')
    
    targetVal = getTargetVal()
        
    numOfRolls = startRolling(targetVal)
    
    print('Got it in {} rolls!'.format(numOfRolls))

if __name__ == '__main__':
    main()