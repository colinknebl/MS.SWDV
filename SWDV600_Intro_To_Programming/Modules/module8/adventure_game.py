# adventure_game.py
#
# A Lord of the Rings Adventure game in which the player is
#  Frodo Baggins trying to destroy the Sauron's ring.

from game_module import Game
from game_text_gui import AdventureGameTextGui
from steps import steps

def main():
    try:
        gui = AdventureGameTextGui()

        game = Game(gui, steps)
        game.play()
    except:
        print('An unexpected error has occurred. The game is shutting down.')
    

if __name__ == '__main__':
    main()