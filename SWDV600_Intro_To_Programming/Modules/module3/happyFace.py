# happyFace.py
#
# A program that draws a happy face using the
#   graphics lib

import graphics as g

def styleEye(eye):
    eye.setFill('white')
    eye.setOutline('aqua')

def main():
    eyeRadius = 25
    
    # create the window
    win = g.GraphWin('Happy Face', 200, 200)
    win.setBackground('lightpink')
    
    # create the pupils
    leftPupil = g.Point(50, 50)
    rightPupil = g.Point(150, 50)
    
    # create the eyes
    leftEye = g.Circle(leftPupil, eyeRadius)
    styleEye(leftEye)
    
    rightEye = g.Circle(rightPupil, eyeRadius)
    styleEye(rightEye)
    
    # draw eyes and pupils
    leftEye.draw(win)
    leftPupil.draw(win)
    rightEye.draw(win)
    rightPupil.draw(win)
    
    # create the nose
    nose = g.Rectangle(g.Point(90, 90), g.Point(110, 140))
    nose.setFill('brown')
    nose.draw(win)
    
    # create mouth line
    centerMouthPoint = g.Point(100, 180)
    leftMouth = g.Line(g.Point(40, 150), centerMouthPoint)
    leftMouth.draw(win)
    
    rightMouth = g.Line(centerMouthPoint, g.Point(160, 150))
    rightMouth.draw(win)
    
main()