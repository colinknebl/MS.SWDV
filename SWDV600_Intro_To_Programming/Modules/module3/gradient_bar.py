# gradient_bar.py
#
# A program to create a color gradient bar

from graphics import *
import math as m
    
def main():
    
    def drawRect(rect, num, color):
        moveX = num * 100
        rect.move(moveX, 0)
        rect.setFill(color)
        rect.setWidth(0)
        rect.draw(win)
    
    # number of rectangles to draw
    numOfRects = 12
    
    # create the window, 400 px wide
    win = GraphWin('Color Gradient', 400, 200)
    
    # create a coordinate system
    win.setCoords(0, 0, numOfRects * 100, 100)
    
    # calculate each step of green
    nextGreen = 255 / (numOfRects - 1)
    
    for rectNum in range(0, numOfRects):
        green = m.floor(rectNum * nextGreen)
        color = color_rgb(0, green, 0)
        drawRect(Rectangle(Point(0,0), Point(200,100)), rectNum, color)
        
main()