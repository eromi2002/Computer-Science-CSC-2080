#File: Module1Homework.py
#Module 1 Homework Questions.

print("Hello, World!")
print("Hello", "world!")
print(3)
print(3.0)
print(2+3)
print(2.0+3.0)
print("2"+"3")
print("2+3=", 2+3)
print(2*3)
print(2**3)
print(7/3)
print(7//3)

#The difference between a and b is that there is a comma between the words.
#The difference between j and k is that j has a multiply symbol, and k has
#2 raised to the power of 3.
    
#Question 5, page 25.

def main():
    print("This program illustrates a chaotic function")
    n=eval(input("How many numbers should I print?"))
    for i in range(n):
        n=3.9 * n * (1-n)
        print(n)

main()

#Question 10 page 55.

#convert.py

def main():
    kilometers=eval(input("Enter the distance in kilometers"))
    miles= kilometers*0.62
    print("The distance is", miles, "miles")

main()

#Question 5, Ch. 2 Online Textbook.

#futval.py
#A program designed to compute the value of an investment
#for a certain number of years.

def main():
    print("This program calculates the future value")
    print("of a 12 year investment")

t=eval(input("Number of years for the investment: "))
t=(10000*(1+(.08/12))**(12*t))



    
    
