# total_service_score.py
#
# Program to calculate the total score based on individual scores


def main():
    
    # prompt the user for how many days of scores they will be entering
    numberOfDays = int(input('How many days of scores? '))

    # initialize the running score
    runningScore = 0

    # loop through each day and ask for that days score
    # then add the daily score to the running score
    for day in range(1, numberOfDays + 1):
        scoreOfDay = int(input('Enter score for day ' + str(day) + ': '))
        runningScore = runningScore + scoreOfDay
        

    # output the total score
    print('The total score of the', numberOfDays, 'days is', runningScore)

main()