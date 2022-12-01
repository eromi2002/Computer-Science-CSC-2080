#File: Module10Homework

#Ch. 11 Discussion Question 1

s1=[2,1,4,3]
s2=['c','a','b']

#a
print(s1 + s2)

#b
print(3 * s1 + 2 * s2)

#c
print(s1[1])

#d
print(s1[1:3])

#e


#Ch. 11 Programming Exercise #6
import random

#Create a list to test shuffle
test_list= [2,3,4,8,7]

#Print the original list
print("The original list is: " +str(test_list))

#Use random.shuffle()
random.shuffle(test_list)

#Print the shuffled list
print("The new shuffled list is: " +str(test_list))

#Ch. 11 Programming Exercise #8

#Create original list
test_list=[2,7,8,7,3,5,3,6]

#Print original list
print("The original list is: " +str(test_list))

#Remove duplicated values
test_list=list(set(test_list))

#Print list after cleaning
print("The new list after removing duplicate values: " + str(test_list))

#Updated Django App
#http://emcoding22.pythonanywhere.com/
