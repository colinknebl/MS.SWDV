# my_house.py
#
# A program that draws a scene of a house

from graphics import *

def main():
    def drawItem(item, color):
        item.setFill(color)
        item.setOutline(color)
        item.draw(win)
        
    # create window
    win = GraphWin('Home Sweet Home', 300, 300, autoflush=False)
    
    # create a coordinate system
    win.setCoords(0, 0, 100, 100)
    
    # draw text
    text = Text(Point(20, 95), 'Home Sweet Home')
    text.setTextColor('blue')
    text.draw(win)
    
    # draw lower sun circle
    sun = Circle(Point(75, 35), 15)
    drawItem(sun, 'yellow')
    
    # draw grass green rectangle
    grass = Rectangle(Point(0, 0), Point(100, 40))
    drawItem(grass, 'green')
    
    # draw house lightblue rectangle
    house = Rectangle(Point(15, 50), Point(45, 15))
    drawItem(house, 'lightblue')
    
    roof = Polygon(Point(13, 50), Point(30, 60), Point(47, 50))
    drawItem(roof, 'darkred')
    
    bottomRightDoor = Point(32.5, 15)
    # draw door brown rectangle
    door = Rectangle(Point(27.5, 27), bottomRightDoor)
    drawItem(door, 'darkred')
    
    # draw right walkway border grey line
    leftLine = Line(bottomRightDoor, Point(35, 0))
    leftLine.setWidth(3)
    drawItem(leftLine, 'grey')
    
    # draw left walkway border grey line
    rightLine = Line(Point(27.5, 15), Point(25, 0))
    rightLine.setWidth(3)
    drawItem(rightLine, 'grey')
    
    # wait for click
    win.getMouse()
    
    for i in range(80):
        sun.move(0, 0.5)
        update(60)
    
main()