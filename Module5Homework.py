#File: Module5Homework.py

#Ch. 6 pg. 206 #1

#farm.py
def main(): 
  for a,n in [("cow","moo"), ("pig", "oink"), ("horse", "nay"), ("sheep", "baa"), ("chicken", "cluck")]:
    verse(a, n)
    print()

def verse(animal, noise):
  refrain()
  hada(animal)
  witha(noise)
  refrain()

def refrain():
  print("Old MacDonald had a farm," ,eieio())

def eieio():
  return ("Ee-igh, Ee-igh, Oh!")

def hada(animal):
  print("And on that farm he had a", animal+",", eieio())

def witha(noise):
  noisecomma = noise + ","
  noise2 = noisecomma + " "+noise
  print("With a", noise2, "here and a", noise2, "there.")
  print("Here a", noisecomma, "there a", noisecomma,"\neverywhere a", noise2+".")


main()

#Ch. 4 pg. 127 #8
from graphics import *
import math

win=GraphWin(width=500,height=400)

win.setBackground('white')

text=Text(Point(250,100),'Click two points to denote the end points of the line')

text.draw(win)

p1=win.getMouse()
p2=win.getMouse()

line=Line(p1,p2)
line.draw(win)

midX=(p1.x+p2.x)/2
midY=(p1.y+p2.y)/2

dot=Circle(Point(midX,midY),3)
dot.setFill('cyan')
dot.draw(win)

dx=abs(p1.x-p2.x)
dy=abs(p1.y-p2.y)

slope=dy/dx
distance=math.sqrt(((p2.x - p1.x)**2 + (p2.y - p1.y)**2))
                   
text.setText('Slope: {:.2f}, distance: {:.2f}. click anywhere to exit'.format(slope,distance))

win.getMouse()

#Ch.3 pg.81 #14

print("This is a program to find the average of a series of numbers")
n1=eval(input("Enter first number: "))
n2=eval(input("Enter second number: "))
n3=eval(input("Enter third number: "))
n4=eval(input("Enter fourth number: "))
average=(n1 +n2 + n3 +n4)/2

print("The average of the numbers is: ", average)


#Ch.6 pg. 207 #12

import random
print("This program returns a random number from a list of numbers")
list= [2, 4, 6, 8]
print("Original list is: " + str(list))
random_num= random.choice(list)
print("Random selected number is: " + str(random_num))

#5

list=[]
n=int(input("Enter number of elements: "))

for i in range(0,n):
  print("Enter element No-{}: " .format(i+1))
  elm= int(input())
  list.append(elm)
print("The entered list is: \n", list)





  

