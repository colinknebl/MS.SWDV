# random_shapes.py
#
# A program to generate random drawings that can be
#  drawn using the shape painter.

# Shape structures
# 
# Circle; 80, 72 (center point); 15 (radius); 32, 208, 86 (color)
# Rectangle; 145, 106 (top left point); 421, 274 (bottom right point); 32, 208, 205 (color)

from random import randrange

# height and width of window
hw = 500

def getUserInput():
    fileName = input('Enter the drawing file name to create: ')
    numOfShapes = int(input('Enter the number of shapes to make: '))
    return fileName, numOfShapes

def writeShapesToFile(fileName, shapes):
    # open file in 'write' mode
    file = open(fileName, 'w')
    # for each shape in shapes, write shape to file
    for shape in shapes:
        file.write(shape)
    # close the file
    file.close()
    return True

def concatStrings(strSeq, seperator=';', addNewLine=True):
    concatStr = ''
    for string in strSeq:
        if concatStr == '':
            concatStr = concatStr + string
        else:
            concatStr = concatStr + seperator + ' ' + string
    if addNewLine:
        concatStr += '\n'
    return concatStr

def getShapeType():
    availableShapes = ['Circle', 'Rectangle']
    return availableShapes[randrange(0, 2)]

def getColorFromDict(colorDict, color):
    colorNum = randrange(colorDict[color][0], colorDict[color][1])
    return str(colorNum)

def getShapeColor():
    colorRangesDict = {
        'red': [10, 55],
        'green': [200, 255],
        'blue': [180, 225]
    }
    colors = []
    for color in colorRangesDict:
        colors.append(getColorFromDict(colorRangesDict, color))
    return concatStrings(colors, seperator=',', addNewLine=False)
    
def getPointCoords(shapeType):
    if shapeType == 'Rectangle':
        ulPtX = randrange(0, hw - 5)
        ulPtY = randrange(0, hw - 5)
        
        lrPtX = randrange(ulPtX, hw)
        lrPtY = randrange(ulPtY, hw)
        
        ulPt = '{}, {}'.format(ulPtX, ulPtY)
        lrPt = '{}, {}'.format(lrPtX, lrPtY)
        return ulPt, lrPt
    else:
        x = randrange(5, hw - 5)
        y = randrange(5, hw - 5)
        return x, y

def getRadius(x, y):
    x1 = x
    x2 = hw - x
    y1 = y
    y2 = hw - y
    
    radiusOpts = [x1, x2, y1, y2]
    radiusOpts.sort()
    maxRadius = radiusOpts[0]
    radius = randrange(0, maxRadius)
    return str(radius)

def generateShapes(numOfShapes):
    shapes = []
    
    for i in range(numOfShapes):
        shape = None
        shapeType = getShapeType()
        shapeColor = getShapeColor()
        if shapeType == 'Circle':
            # generate center point
            x, y = getPointCoords(shapeType)
            # generate radius
            radius = getRadius(x, y)
            # stringify the center point
            centerPt = '{}, {}'.format(x, y)
            # build shape string
            shape = concatStrings([shapeType, centerPt, radius, shapeColor])
        else:
            # get rectangle points
            ulPt, lrPt = getPointCoords(shapeType)
            # build shape string
            shape = concatStrings([shapeType, ulPt, lrPt, shapeColor])
        shapes.append(shape)
    return shapes
    
def main():
    # get user input
    fileName, numOfShapes = getUserInput()
    
    # generate shapes
    shapes = generateShapes(numOfShapes)
    
    # write shapes to file
    writeShapesToFile(fileName, shapes)
    
if __name__ == '__main__':
    main()