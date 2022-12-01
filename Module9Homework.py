#File: Module9Homework.py

#Ch. 10 pg.356  True/False 1-5

#1 True

#2 False

#3 False

#4 False

#5 False

#Ch. 10 pg. 357 Multiple Choice 1-5

#1 A= def

#2 A= three

#3 C= import statement

#4 B=self.x

#5 C= an underscore_

#Ch. 10 pg. 357 Discussion Question 1

#With instance variables, values of variables can change depending on the object,
#while regular variables do not use the instance method, and are defined inside
#of a class.

#Ch.10 pg. 360 Programming Exercise #9

class Spheres:
    def __init__(self, radius):
        self.radius=r
        self.area=0
        self.volume=0

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        r=self.radius
        self.area=4*3.14*(r*r)
        return (self.area)

    def getVolume(self):
        r=self.radius
        self.volume=(4/3)*3.14*(r*r*r)
        return(self.volume)

#Ch. 3 Programming Exercise 1

class Spheres:
    def __init__(self, radius):
        self.radius=r
        self.area=0
        self.volume=0

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        r=self.radius
        self.area=4*3.14*(r*r)
        return (self.area)

    def getVolume(self):
        r=self.radius
        self.volume=(4/3)*3.14*(r*r*r)
        return(self.volume)

#PythonAnywhere link
#http://emcoding22.pythonanywhere.com/
