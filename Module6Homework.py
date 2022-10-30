#Module6Homework.py

#Ch. 7 pg.237 #2

#Try-except statements are similar to if-elif-else statements because they are both
#decision structures, but try-except statments are usually based on
#logical conditions, where if-elif-else statements are.

#Ch. 7 pg. 239 #3

print("This program calculates your grade")

scores=int(input("Enter current grade for Computer Science: "))
if scores>90:
    grade='A'
elif scores>80:
    grade='B'
elif scores>=70:
    grade='C'
elif scores>60:
    grade='D'
else:
    grade='F'

print("\nGrade is: " + grade)

#Ch. 7 pg.239 #7

import math

print("This program calculates the total amount earned for babysitting")

print("Enter starting hours: ")
stime_hours=int(input("Enter starting time: "))
print("minutes")
stime_minutes=int(input())

print("Enter ending time in hours")
etime_hours=int(input())
print("minutes")
etime_minutes=int(input())

cost=2.50

if (stime_hours<21 and etime_hours>21):
    a_hours=etime_hours-21
    a_minutes=etime_minutes

    time_minutes=60-stime_minutes
    time_hours=21-(stime_hours+1)
    time_hours=time_hours*60
    time=time_hours+time_minutes

    cost=(cost/60)*time
    time=(a_hours*60)+a_minutes
    cost=cost+(1.75/60)*time

    ptint("cost=$", cost)
elif(stime_hours>=21):
    time_hours=et_hours-(stime_hours+1)
    time_minutes=(60-stime_minutes)+etime_minutes
    time=(time_hours*60)+time_minutes
    cost=(1.75/60)*(time)
    print("cost=$",cost)

elif(etime_hours<=21):
    time_hours=etime_hours-(stime_hours+1)
    time_minutes=(60-stime_minutes)+etime_minutes
    time(time_hours*60)+time_minutes
    cost=(2.50/60)*time
    print("cost=$",cost)

    
#Ch. 7 pg. 239 #8

print("This program tells your ability to run for the Senate and House")

age=int(input("Enter your current age: "))
if age>=30:
    eligibility='Yes!'
elif age>=25:
    eligibility='Yes!'
else:
    eligibility='No, sorry'

print("\nEligibility is: " + eligibility)

citizen=int(input("Enter how long you have been a citizen of the United States: "))
if citizen>=9:
    eligibility='Yes!'
elif citizen>=7:
    eligibility='Yes!'
else:
    eligibility='No, sorry'

print("\nEligibility is: " + eligibility)
    
#5 Modified Program

list=[]
n=int(input("Enter number of elements: "))
if n>1:
    acceptance="You're good to go"
elif n==1:
    acceptance= "You're good to go"
else:
    acceptance="Error, can't have less than 1 element"
print("\nAcceptance is: " + acceptance)

for i in range(0,n):
  print("Enter element No-{}: " .format(i+1))
  elm= int(input())
  list.append(elm)
print("The entered list is: \n", list)

