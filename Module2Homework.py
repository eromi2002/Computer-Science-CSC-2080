#File: Module2Homework.py
import math as math

#Ch. 2 pg.53 #4 (a, b , c, d)

#a
for i in range(5):
    print(i*i)

#b
for d in [3,1,4,1,5]:
    print(d,end=" " )

#c
for i in range(4):
    print("Hello")

#d
for i in range(5):
    print(i, 2**i)

#Ch. 3 pg. 77/78 #1, (a, c, e)

#a
ans= eval("4.0/10.0 + 3.5 * 2")
print(ans)

#b
ans= eval("(4-20 // 3) ** 3")
print(ans)

#c
ans=eval("3 * 10 // 3 + 10 % 3")
print(ans)


#Ch.3 pg.78 #2 (b,c)

#b
n=2
n*n *(n-1)/2
print(n*(n-1)/2)

#c
r=4
4*math.pi*r**2
print(4*math.pi*r**2)


#Ch. 3 pg. 78 #4 (b, c)

#b
for i in [1,3,5,7,9]:
    print(1, ":", i**3)
    print(i)
    
#c
x=2
y=10
for j in range(0, y, x):
    print(j, end=" ")
    print(x + y)
print("done")


#Ch. 3 pg. 80 (#6, #7)

#6
x1=eval(input("Enter a value for x1: "))
x2=eval(input("Enter a value for x2: "))
y1=eval(input("Enter a value for y1: "))
y2=eval(input("Enter a value for y2: "))
ans=eval(input(y2-y1/x2-x1))
print(ans)

#7

discRoot=math.sqrt((x2*x1) * (x2*x1)) + ((y2*y1) * (y2-y1))
x2=eval(input("Enter value for x2: "))
x1=eval(input("Enter value for x1: "))
y2=eval(input("Enter value for y2: "))
y1=eval(input("Enter value for y1: "))
print(ans)




