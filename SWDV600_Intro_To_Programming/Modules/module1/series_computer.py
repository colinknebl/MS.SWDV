totalScore = 0
for game in range(1, 4):
    gameScore = int(input('What was your score for game ' + str(game) + '? '))
    totalScore = totalScore + gameScore
    
print('Your total score is: ', totalScore)