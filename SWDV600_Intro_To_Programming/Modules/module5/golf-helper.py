# golf-helper.py
#
# A program that helps the user decide what golf club they should use.

def main():
    # print intro message
    print('Welcome to the Golf Club Helper!', 
    '\nTell me your situation, and I\'ll recommend a club\n')
    
    # ask user if they hit on the green
    ballOnGreen = input('Did you hit it on the green (y/n)? ') == 'y'
    distance = int(input('How far is the ball from the hole? '))
    
    recommendedClub = None
    if ballOnGreen:
        recommendedClub = 'Putter'
    elif distance >= 200:
        recommendedClub = 'Driver'
    elif distance >= 140:
        recommendedClub = '5-Iron'
    elif distance >= 100:
        recommendedClub = '9-Iron'
    else:
        recommendedClub = 'Pitching Wedge'
        
    # print recommendation
    print('\nI recommend using your {}'.format(recommendedClub))

main()