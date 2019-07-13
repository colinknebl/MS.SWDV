def printGoTeam():
    print('Go, team, go!')
    print('Defeat your foe.')

def printStanza():
    printGoTeam()
    print('Simply the best,')
    print('Better than the rest.')
    printGoTeam()
    print('')

def sing_fight_song():
    printGoTeam()
    print('')
    for i in range(2):
        printStanza()
    printGoTeam()

sing_fight_song()