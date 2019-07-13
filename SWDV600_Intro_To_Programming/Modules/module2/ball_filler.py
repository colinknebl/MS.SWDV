# ball_filler.py
#
# Program to calculate the amount of filler required
# for the user specified amount of balls

import math

def main(): 

    # get the number of balls
    numberOfBalls = int(input('How many bowling balls will be manufactured? '))

    # get the ball diameter
    ballDiameter = float(input('What is the diameter of each ball in inches? '))

    # get the core volume
    coreVolume = float(input('What is the core volume in inches cubed? '))

    # calculate ball radius
    ballRadius = ballDiameter / 2

    # calculate ball volume
    ballVolume = (4/3) *  (math.pi * ballRadius ** 3)

    # calculate filler volume
    fillerVolume = ballVolume - coreVolume

    # calculate total volume
    totalVolume = fillerVolume * numberOfBalls

    # print the results
    print('You will need ' + str(totalVolume) + ' inches cubed of filler')

main()