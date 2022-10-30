#File: Module7Homework.py

#Ch. 7 pg. 278 #1

#a A definite loop can have a specific amount of times that the loop will be executed,
#and an indefinite loop has an unknown amount of times that it will be executed.

#b A for loop executes the amount of times as given in the first expression.
#a while loop continues as long as the input continues to be true based on the first expression.

#c An interactive loop allows the user to repeat certain parts of the program as needed,
# and a sentinel loop continues to process data until it reaches a certain value that signals it to end.

#d A sentinel loop continues to process data until it reaches a certain value that signals it to end.
# and a end-file loop 

#Ch. 7 pg. 278/279 #2

#Work for truth tables sent in email. Not sure how to create tables in code.

#a
#P   #Q    #P&Q    #not (P and Q)


#Ch. 7 pg. 279 #3

#a
total=0
for num in range(n+1)
   total+=num

#b
total=0
for num in range(n*n):
   if num % 2==1
   total+=num

#c
total=0
user_num=eval(unput("Enter a number, 999 to quit: "))
while user_num !=999
   total+=user_num
   user_num=eval(input("Enter a number, 999 to quit: "))

#d
counter=0
while n !=1
   n=n//2
   counter +=1

#Ch. 7 pg. 279 #1
nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
 
#Ch. 7 pg. 280 #4

def syracuse(n, acc=None):
    if acc is None:
        acc = []  
    if n == 1:
        acc.append(n)
        return acc
    elif n % 2 == 0:
        n /= 2
        acc.append(n)
        return syracuse(n, acc)
    else:
        n = (n*3) + 1
        acc.append(n)
        return syracuse(n, acc)
