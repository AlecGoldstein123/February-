'''import turtle as t
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)'''
'''
import turtle as t 
def square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

square(150)
square(200)
square(250)
square(300)
'''

import turtle as t

def right ():
    t.left(90)
    t.left(90)
    t.left(90)

def drawStep():
    t.forward(50)
    t.left(90)
    t.forward(50)
    right()

def drawSide():
    drawStep()
    drawStep()
    drawStep()
    t.forward(50)
    t.right(90)

def drawDiamond():
    drawSide()
    drawSide()
    drawSide()
    drawSide()
drawDiamond()
       
