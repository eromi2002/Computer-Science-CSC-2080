#File: Module4Homework.py

#Ch.5 pg. 169 #1 (c,e,g)

#c
s1="spam"
s2="ni!"
print(s1[1])

#e
s1="spam"
s2="ni!"
print(s1[2] + s2[:2])

#g
s1="spam"
s2="ni!"
print(s1.upper())

#Ch.5 pg. 170 #2 (a,d,e)

#a
s1="spam"
s2="ni!"
print("NI")

#d
s1="spam"
s2="ni!"
print("spam")

#e
s1="spam"
s2="ni!"
print(["sp","m"])

#Ch.5 pg.170 #3 (b,c,e)

#b
for w in "Now is the winter of our discontent...".split():
    print(w)

#c
for w in "Mississippi".split("i"):
    print(w, end=" ")

#e
msg= " "
for ch in "secret":
    msg=msg+chr(ord(ch)+1)
    print(msg)

#Special Program
strings = ["FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"]
           
strings2 = ["DDDDDDDDDD"]

strings3 = ["CCCCCCCCCC"]

strings4 = ["BBBBBBBBBB"]

strings5 = ["AAAAAAAAAA"]

for i in range(len(strings)):
    print(strings[i], end='')

for i in range(len(strings)):
    print(strings2[i], end='')

for i in range(len(strings)):
    print(strings3[i], end='')

for i in range(len(strings)):
    print(strings4[i], end='')

for i in range(len(strings)):
    print(strings5[i], end='')
    
#Ch.5 pg.171 #3
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

#Ch.5 pg. 171 #4
Phrase=input("Enter a Phrase to convert to acronym: ")
list_words=Phrase.split()
final_acro=" "
for i in list_words:
    final_acro+=i[0].upper()

print("Final Acronym: ",final_acro)

#Ch.5 pg.171 #5
name= input("Enter your full name: ").lower()
print()
print (sum(ord(ch)-96 for ch in name))




    

