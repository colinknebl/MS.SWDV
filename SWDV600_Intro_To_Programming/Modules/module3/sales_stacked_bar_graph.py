# sales_stacked_bar_graph.py
#
# A program that enables a user to enter the
#   number of donuts sold over the past three days

# 1. enable the user to enter the sales numbers
#    for three days, one at a time
# 2. draw a single, stacked bar graph of each day’s
#    sales adding to the stack after a day of sales is entered
# 3. display the number of sales for the day within it's
#    corresponding box in the stacked bar graph
# 4. display the total number of sales over the three days
# 5. display the average number of sales over the three days

import graphics as g

def main():

    def drawRectangle(i, salesNum):
        print('num', salesNum)
        p1x = i * 100
        p1y = 85
        p2x = p1x + 100
        p2y = 140
        rectangle = g.Rectangle(g.Point(p1x, p1y), g.Point(p2x, p2y))
        rectangle.draw(win)
        g.Text( g.Point( i * 100 + 50, 112 ), salesNum ).draw( win )
        
    
    def addToTotal(total, salesNum):
        return total + salesNum
    
    def calcAvg(total):
        return total / 3
    
    def printTotalAndAvg(total, avg):
        g.Text(g.Point(60, 180), 'Total: ' + str(total)).draw(win)
        g.Text(g.Point(280, 180), 'Average: ' + str(avg)).draw(win)
    
    # initialize window
    win = g.GraphWin('Donuts Sold', 640, 200)
    
    # draw entry box for sales numbers
    g.Text( g.Point( 60, 40 ), 'Enter Sales: ' ).draw( win )
    entry = g.Entry(g.Point(140, 40), 10)
    entry.setFill('white')
    entry.draw(win)
    
    # draw axis line
    g.Line(g.Point(100, 75), g.Point(100, 150)).draw(win)
    
    # initialize running total
    total = 0
    
    for clickCount in range(1, 4):
        clickPoint = win.getMouse()
        userEntry = int(entry.getText())
        drawRectangle(clickCount, userEntry)
        total = addToTotal(total, userEntry)
    
    print('total', total)
    avg = calcAvg(total)
    print('average', avg)
    
    printTotalAndAvg(total, avg)
    
main()