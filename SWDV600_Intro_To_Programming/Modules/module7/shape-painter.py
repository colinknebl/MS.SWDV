# shape-painter.py
#
# A program to read rectangles and circles from
#  an input file and then draw them in a window

from graphics import *

def getPoint(pointString):
    x, y = pointString.split(',')
    return Point(int(x), int(y))

def getColor( colorString ):
    tokens = colorString.split(',')
    if len(tokens) == 3:
        return color_rgb(int(tokens[0]), int(tokens[1]), int(tokens[2]))
    elif colorString == '':
        return 'white'
    else:
        return colorString.strip()

def getRadius(radiusString):
    return int(radiusString)

def parseCircleLine(line):
    'Circle; 400, 200; 50; 72, 92, 244'
    shapeStr, centerPtStr, radiusStr, colorStr = line.split(';')
    circle = Circle(getPoint(centerPtStr), getRadius(radiusStr))
    circle.setFill(getColor(colorStr))
    return circle

def parseRectangleLine(line):
    'Rectangle; 51, 20; 63, 70; red'
    shapeStr, ulPtStr, lrPtStr, colorStr = line.split(';')
    rect = Rectangle(getPoint(ulPtStr), getPoint(lrPtStr))
    rect.setFill(getColor(colorStr))
    return rect

def getShapeName(line):
    tokens = line.split(';')
    return tokens[0]

def getShapes(file):
    shapes = []
    lineCount = 0
    for line in file.readlines():
        lineCount += 1
        shapeName = getShapeName(line)
        shape = None
        if shapeName.casefold() == 'Circle'.casefold():
            shape = parseCircleLine(line)
        elif shapeName.casefold() == 'Rectangle'.casefold():
            shape = parseRectangleLine(line)
        else:
            raise ValueError('ERROR on line {}: Invalid shape \'{}\''.format(lineCount, shapeName))
        
        shapes.append(shape)
    return shapes

def drawShapes(shapes):
    win = GraphWin('Shapes', 500, 500)
    for shape in shapes:
        shape.draw(win)

def main():
    # open file in read
    fileName = input('Input the file name: ')
    shapesFile = open(fileName, 'r')
    
    shapes = getShapes(shapesFile)
    
    drawShapes(shapes)
    
    shapesFile.close()

if __name__ == '__main__':
    main()