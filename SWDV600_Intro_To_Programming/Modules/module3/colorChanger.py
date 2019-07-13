# colorChanger.py
#
# A program that changes the backgound color of the
#  window as the user clicks. After 3 clicks the
#  window closes

import graphics as g
from graphics import *

def main():
    win = GraphWin('Click in the window', 320, 320)
    win.setBackground(g.color_rgb(0, 100, 0))

    red = 0
    green = 100
    blue = 0

    for clickCount in range(3):
        print(clickCount)
        clickPoint = win.getMouse()
        red = red + 0
        green = green + 50
        blue = blue + 0
        win.setBackground(g.color_rgb(red, green, blue))
    
    win.close()
        
main()