#Module8Homework.py

#Ch. 9 Discussion Question 1 pg. 308

#Start the program
#Print an introduction
#Ask user for dimensions on length and width
#Get program to compute total dimensions needed
#Print results

#Ch. 9 Programming Exercise 1 pg. 309

from random import random

def main():
    printIntro()
    probA, probB, n=getInputs()
    winsA. winsB=simNGames(n,probA,probB)
    printSummary(winsA,winsB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by the probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    #Returns the three simulation parameters
    a=float(input("What is the prob. player A wins a serve? "))
    b=float(input("What is the prob. player B wins a serve? "))
    n =int(input("Best of how many games?: "))
    return a, b , n

def simNGames(n, probA, probB):
    #Simulate n games of racquetball between players whose
    #abilities are represented by the probability of winning a serve.
    #Returns number of wins for A and B
    winsA=winsB=0
    while winsA <=2 and winsB <= n/2:
        game +=1
        if game %2==0:
            scoreA, scoreB=simOneGame(probA, probB, "B")
        else:
            scoreA, scoreB= simOneGame(probA, probB, "A")
        if scoreA>scoreB:
            winsA <=winsA +1
        else:
            winsB=winsB +1
    return winsA, winsB

def simOneGame(probA, probB):
    #Simulate a single game or racquetball between players whose
    #abilities are represented by the probability of winning a serve.
    #Returns number of wins for A and B.
    serving="A"
    scoreA=0
    scoreB=0
    while not gameOver(scoreA,scoreB):
        if serving=="A":
            if random()<probA:
                scoreA +=1
            else:
                serving="B"
        else:
            if random()<probB:
                scoreB +=1
            else:
                serving="A"
    return scoreA, scoreB

def gameOver(a,b):
    #a and b represent scores for a racquetball game
    #Returns true if the game is over, False otherwise.
    return a==15 or b==15

def printSummary(winsA,winsB):
    #Prints summary of wins for each player.
    n=winsA +winsB
    print("\nGames simulates: ", n)
    print("Wins for A: {0} ({1:0.1%})" .format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})" .format(winsB, winsB/n))

if __name__ == '__main__':
    main()

#Ch. 9 Programming Exercise #2 pg. 309

    from random import random

def main():
    printIntro()
    probA, probB, n=getInputs()
    winsA, winsB, shutoutsA, shutoutsB=simNGames(n,probA,probB,shutoutsA,shutoutsB)
    printSummary(winsA,winsB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by the probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    #Returns the three simulation parameters
    a=float(input("What is the prob. player A wins a serve? "))
    b=float(input("What is the prob. player B wins a serve? "))
    n =int(input("Best of how many games?: "))
    return a, b , n

def simNGames(n, probA, probB):
    #Simulate n games of racquetball between players whose
    #abilities are represented by the probability of winning a serve.
    #Returns number of wins for A and B
    winsA=winsB=0
    shutoutsA=shutoutsB=0
    for i in range(n):
        scoreA, scoreB= simOneGame(probA, probB)
        if scoreA > scoreB:
             winsA +=1
             if scoreB ==0:
                 shutoutsA +=1
        else:
            winsB=1
            if scoreA==0:
                shutoutsA +=1
    return winsA, winsB, shutoutsA, shutoutsB

def simOneGame(probA, probB):
    #Simulate a single game or racquetball between players whose
    #abilities are represented by the probability of winning a serve.
    #Returns number of wins for A and B.
    serving="A"
    scoreA=0
    scoreB=0
    while not gameOver(scoreA,scoreB):
        if serving=="A":
            if random()<probA:
                scoreA +=1
            else:
                serving="B"
        else:
            if random()<probB:
                scoreB +=1
            else:
                serving="A"
    return scoreA, scoreB

def gameOver(a,b):
    #a and b represent scores for a racquetball game
    #Returns true if the game is over, False otherwise.
    return a==15 or b==15

def printSummary(winsA,winsB):
    #Prints summary of wins for each player.
    n=winsA +winsB
    print("\nGames simulates: ", n)
    print("Wins for A: {0} ({1:0.1%})" .format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})" .format(winsB, winsB/n))
    print("Shutouts won by A: {0} ({1:0.1%})" .format(shutoutsA, shutoutsA/n))
    print("Shutouts won by B: {0} ({1:0.1%})" .format(shutoutsB, shutoutsB/n))

if __name__ == '__main__':
    main()

#API Summary
    
#API stands for "Application Programming Interface", and it is a list of rules that a website follows to share
#data with other applications. An API endpoint is a location that is shown from the API that collects the data.
#An example of a modern API are bots that appear in comments after using certain words in the original post.
#For example, if the user posts something with the word "homework help" or "essay", homework help
#bots will flood the replies.
