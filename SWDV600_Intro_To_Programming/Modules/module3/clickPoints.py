from graphics import *


win = GraphWin( 'Click to see coordinates', 640, 320 )

for clickCount in range(10):
    clickPoint = win.getMouse()
    Text( clickPoint, clickPoint ).draw( win )

