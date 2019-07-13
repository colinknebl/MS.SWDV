from random import random


def printWelcomeMessage():
    print('Welcome to the racquetball simulation!')
    
def getInputValues():
    probA = float(input('probability player A will score on their serve: '))
    probB = float(input('probability player B will score on their serve: '))
    simNGames = int(input('Number of games to simulate: '))
    playerAServesFirst = input('Which player will server first (A/B)? ') in 'Aa'
    return probA, probB, simNGames, playerAServesFirst

def printResults( winsA, winsB ):
    totalGames = winsA + winsB
    print('wins for player A: {0} {1:0.1f}%'.format(winsA, 100 * winsA / totalGames))
    print('wins for player B: {0} {1:0.1f}%'.format(winsB, 100 * winsB / totalGames))

def gameOver(scoreA, scoreB):
    return scoreA == 15 or scoreB == 15

def simGame(probA, probB, playerAServesFirst):
    scoreA, scoreB = 0, 0
    playerAServing = playerAServesFirst
    while not gameOver(scoreA, scoreB):
        if playerAServing:
            if random() < probA:
                scoreA += 1
            else:
                playerAServing = False
        else: # player B is serving
            if random() < probB:
                scoreB += 1
            else:
                playerAServing = True
    
    return scoreA, scoreB

def simNGames( simNGames, probA, probB, playerAServesFirst ):
    winsA, winsB = 0, 0
    for game in range(simNGames):
        scoreA, scoreB = simGame(probA, probB, playerAServesFirst)
        if scoreA == 15:
            winsA += 1
        else:
            winsB += 1
    
    return winsA, winsB

def main():
    printWelcomeMessage()
    probA, probB, numOfGames, playerAServesFirst = getInputValues()
    winsA, winsB = simNGames( numOfGames, probA, probB, playerAServesFirst )
    printResults( winsA, winsB )
    
if __name__ == '__main__':
    main()