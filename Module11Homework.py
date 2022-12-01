#File: Module11Homework.py

#Programming Exercise Number 5

from random import randrange

class Dice:
    def __init__(self):
        self.dice=[0]*2
        self.rollDice()

    def rollDice(self):
        for i in range(len(self.dice)):
            self.dice[i]=randrange(1,7)
    
    def values(self):
        return self.dice[:]

class SkunkApp:
    def __init__(self, interface):
        self.dice=Dice()
        self.interface=interface
        self.players=[]
        self.makeplayers()

    def run(self):
        while not self.gameOver():
            self.interface.newRound()
            self.refreshPlayers()
            print("Round: {}".format(self.interface.getRound() +1))
            print("\n")
            self.playRound()
        self.interface.gameSummary(self.players)

    def playRound(self):
        books=self.interface.getRound()
        while not self.roundOver():
            for player in self.players:
                if player.active():
                    values=self.doRoll(player)
                    if values !=[0,0]:
                        x,y=values[0], values[1]
                        if x==1 or y==1:
                            player.resetRoundScores(books)
                        elif x==1 or y==1:
                            player.reset_rScore()
                        else:
                            player.inc_Score(x+y, books)
                        self.interface.currentscores(values, self.players)
        for player in self.players:
            player.tallyRound(books)

    def refreshPlayers(self):
        for player in self.players:
            player.reactivate()
            player.rScoreOnly()

    def doRoll(self, player):
        if self.interface.rollAgain(player.getName()):
            self.dice.rollDice()
            values=self.dice.values()
            return values
        else:
            player.deactivate()
            return[0,0]
    def makeplayers(self):
        for name in self.interface.getPlayerNames():
            x=Player(name)
            self.players.append(x)

    def roundOver(self):
        over=True
        for player in self.players:
            if player.activate():
                over=False
        return over

    def gameOver(self):
        if self.interface.getRound() >=4:
            return True

class Player:
    def __init__(self, name):
        self.name=name
        self.rScore=0
        self.totScore=0
        self.roundScores=[0]*5
        self.play=True

    def getName(self):
        return self.name

    def tallyRound(self, book):
        self.roundScores[book]=self.get_rScore()

    def resetRoundScore(self,books):
        prevRoundScores=0
        for num in self.roundScores:
            prevRoundScores += num
        self.totScore -= prevRoundScores
        for i in range(books):
            self.roundScores[i]=0
        self.play=False

    def inc_Score(self, score, books):
        self.totScore=self.totScore + score
        prevRoundScores=0
        for num in self.roundScores[0:books]:
            prevRoundScores += num
        self.rScore=self.totScore - prevRoundScores

    def reset_rScore(self):
        self.totScore -= self.rScore
        self.rScore=0
        self.play=False

    def get_rScore(self):
        return self.rScore

    def get_roundScores(self):
        return self.roundScores

    def get_totScore(self):
        return self.totScore

    def reactivate(self):
        self.play=True

    def deactivate(self):
        self.play=False

    def rScoreOnly(self):
        self.rScore=0

class TextInterface:
    def __init__self(self):
        self.round= -1

    def getRound(self):
        return self.round

    def newRound(self):
        self.round=self.round +1
        return self.round
        print()
        print("Entering round {}".format(self.__whichRound()))

    def setDice(self,values):
        print("You rolled {}.".format(values))
        print("\n")

    def __whichRound(self):
        letter= ["S", "K", "U", "N", "K"]
        return letter[self.round]

    def gameOver(self, name):
        print("Game Over. {} wins!".format(name))

    def currentscores(self, values, players):
        for player in players:
            name=player.getName()
            rScore=player.get_rScore()
            totscore=player.get_totScore()
            print("Player: {0} Score: {1} Total: {2}".format(name, rScore, totscore))
        self.setDice(values)

    def finalScores(self,players):
        print("Name: {0:>10}{1:>10}{2:>10}{3:>10}{4:>10}{5:>10}".format(
            "S", "K", "U", "N", "K", "Total"))
        print("--------------------------------------------------------")
        for player in players:
            scores=player.get_roundScores()
            name=player.getName()
            totscore=player.get_totScore()
            print("{0:5}:{1:>10}{2:>10}{3:>10}{4:>10}{5:>10}{6:>10}".format(
                name, scores[0], scores[1], scores[2], scores3[], scores[4], totscore))

    def rollAgain(self, name):
            ans=None
            while ans==None:
                ans=input(
                    "Enter Y/y if you want to roll again and N/n if \ you don't {}? >>".format(name))
                if ans[0] in "yY":
                    return True
                elif ans[0] in "nN":
                    return False
                else:
                    ans=None
                    print("Sorry, I don't understand.")

    def getPlayerNames(self):
                totplayers=[]
                x=0
                while x !='':
                    x=input("Enter players name (<Enter> to Continue) >>")
                    totplayers.append(x)
                    totplayers.remove('')
                    return totplayers
     def gameSummary(self,players):
                print("The game is over.")
                self.finalScores(platers)
def main():
    inter= TextInterface()
    app=SkunkApp(inter)
    app.run()

main()

#Programming Exercise #7

from card import Card, Hand, Deck
from time import sleep

class War:
    def __init__(self, deck, inter):
        deck.shuffle()
        self.deck=deck
        self.interface=inter
        self.player1= Hand(self.deck.deck[::2])
        self.player2= Hand(self.deck.deck[1::2])
        self.win_deck1= []
        self.win_deck2= []

    def play(self):
        round=1
        while not self.game_over():
            self.interface.round()
            self.flip_cards()
            if self.player1.cards_left()==0 and len(self.win_deck1) !=0:
                self.shuffle_in_win_Deck('player 1')
            if self.player2.cards_left()==0 and len(self.win_deck2) !=0
                self.shuffle_in_win_deck('player 2')
            round +=1
        self.winner(self.determine_winner())

    def flip_cards(self_:
        p1_card=self.player1.flip_card()
        p2_card=self.player2.flip_card()
        self.winning_hand(p1_card, p2_card)

    def winning_hand(self, p1_card, p2_card, war_count=0):
        self.interface.cards(p1_card, p2_card)
        if p1_card.value() > p2_card.value():
            if war_count==0:
                self.win_deck1.append(Self,player1.pop(0))
            self.win_deck1.append(Self.player2.pop(0))
            self.interface.winning_hand('player 1')
        else:
            self.interface.winning_hand('player 1)
            for card in self.player1.pop_multi(range(4*war_count +1)):
                self.win_deck1.append(card)
            for card in self.player2.pop_multi(range(4*war_count +1)):
                self.win_Deck1.append(card):
        elif p2_card.value() >p1_card.value():
            if war_count ==0:
                self.win_deck2.append(self.player.pop(0))
                self.win_deck2.append(self.player2.pop(0))
                self.interface.winning_hand('player 2')
            else:
                self.interface.winning_hand('player 2')
                for card in self.player1.pop_multi(range(4*war_count +1)):
                    self.win.deck_2.append(card)
                for card in self.player2.pop_multi(range(4*war_count +1)):
                    self.win_deck1.append(card)
        else:
            self.war(war_count)

        def war(Self, count):
            count+=1
            if self.player1.cards_left() >= 4*count and\
               self.player2.cards_left() >= 4*count:
                self.interface.war()
                self.winning_hand(self.player1.flip_card(4*count),
                                  self.player2.flip_card(4*count), count)
            elif self.player1.cards_left() < 1 + 4*count:
                self.player1=Hand([])
            else:
                self.shuffle_in_win_deck('player 2')
                if self.player2.cards_left() <1 +4*count:
                    self.player2= Hand([])
                    
        def shuffle_in_win_deck(self, player):
            if player=='player 1':
                self.player1=Hand(self.win_deck1[:])
                self.player1.shuffle()
                self.win_deck1=[]
            else:
                self.player2=Hand(self.win_deck2[:])
                self.player2.shuffle()
                self.win_deck2=[]

        def game_over(self):
            return self.player1.cards_left() ==0 or self.player2.cards_left()==0

        def determine_winner(self);
            if self.player1.cards_left()==0:
                return self.player2
            else:
                return self.player1
            
        def winner(self, hand):
            if hand==self.player1:
                self.interface.win_screen('player 1')
            elif hand==self.player2:
                self.interface.win_screen('player 2')
            else:
                print('Something went wrong')
                
    class Interface:
        def round(self, num):
            print('\nRound', num)

        def cards(self, comp_card, plyr_Card):
            print('The computer draws a ', comp_card)

        def winning_hand(self, player):
            if player=='player 2':
                print('You can win the hand.')
            else:
                print('The computer wins the hand.')

        def war(self):
            print('I...')
            sleep(1)
            print('De...')
            sleep(1)
            print('Clare...')
            sleep(1)
            input('Press any key to exit')
            print('War!')

        def win_screen(self, player):
            if player=='player 1':
                print('\nYou\'re out of cards. The computer wins.')
                input('Press any key to exit')
            else:
                print('\nThe computer is out of cards. You win!')
    i
    f __name__ == '__main__':
        deck=Deck()
        inter=Interface()
        war_game=War9deck, inter)
        war_game.play()
                
            

        
                
            
                                        
        
                   
        
                    
