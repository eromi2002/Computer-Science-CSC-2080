#File: Module3Homework.py

from graphics import *
win= GraphWin()

#Ch.3 Pg.81 (#13, #14)

#13
print("This is a program to sum a series of numbers")
n1=eval(input("Enter first number: "))
n2=eval(input("Enter second number: "))
number1, number2 =eval(input("Enter two score separated by a comma: "))
for i in range(5):
    average=(n1 + n2)/2


print("The average of the numbers is: ",average)
                  
    
#14
print("This is a program to find the sum of numbers")
number1=eval(input("Enter the first number: "))
number2=eval(input("Enter the second nunber "))
average= (number1 + number2)/2
print("The average of the numbers is: ", average)


#Ch. 4 Pg. 125 (#2 a-g)

#a
#A point on the window at the set point of (130,130)

#b
#A blue circle outlined in red at a certain point.

#c
#A rectangle filled in with a blend
#of red blue and green, a width of 3, and at a specific point. 

#d
#A dark red line with an arrow head, and set to start and stretch
#to a certain point.

#e
#An oval centered at a certain point with a specific radius.

#f
#A polygon that is filled in orange, and centered at a specific point.

#g
#The following prints the text "Hello World!", set to the font courier, font size
#16, and set to the italic font face.

#Ch. 3 Pg. 128 (#3)
#A red circle appears at the point specified in the code,
#When the user clicks the blank space, the circle moves to that spot,
#And then the program closes.

#Ch. 4 Pg. 126 (#2, #3, #8)

#2

def main():
    win=GraphWin('Archery Target', 200,200)
center=Point(100,100)

w=Circle(center, 10)
w.setFill('white')
w.setOutline('black')
w.draw(win)

bl=Circle(center, 60)
bl.setFill('black')
bl.setOutline('white')
bl.draw(win)

b=Circle(center, 40)
b.setFill('blue')
b.setOutline('white')
b.draw(win)

r=Circle(center, 20)
r.setFill('red')
r.setOutline('white')
r.draw(win)

y=Circle(center, 10)
y.setFill('yellow')
y.setOutline('black')
y.draw(win)

win.getMouse()
win.close()

main()


#3
circ=Circle(Point(100,100), 50)
win=GraphWin()
circ.setFill('yellow')
circ.setOutline('black')
circ.draw(win)

leftEye=Circle(Point(130,100), 5)
leftEye.setFill('black')
leftEye.setOutline('white')
leftEye.draw(win)
rightEye=Circle(Point(70,100), 5)
rightEye.setFill('black')
rightEye.setOutline('white')
rightEye.draw(win)

Line(Point(90,120), Point(110,120)).draw(win)

win.getMouse()
win.close()

#8
import math
def main():
    win = GraphWin("Click Me!")
    for i in range(10):
        i=Line(Point(20,20), Point(110,120)).draw(win)
        p = win.getMouse()
        print("You clicked at:", p.getX(), p.getY())
    
main()


