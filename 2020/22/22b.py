import os
import re
import common.util as u
#import common.comp as c
import logging
import time
import copy
import math
import queue
count = 0

#data = u.readfile(u.AOC_2020 + "\\22\\input_ex.txt")
data = u.readfile(u.AOC_2020 + "\\22\\input.txt")
round_count = 0

class Game:
    OPP = [1,0]
    VERBOSE = True
    def __init__(self,decks,id):
        self.previousDeck1 = []
        self.previousDeck2 = []
        self.gw = -1
        self.decks = decks
        self.origDecks = [decks[0].copy(),decks[1].copy()]
        self.numPlayers = len(decks)
        self.id = id
        self.roundNumber = 0
        if self.id == 0:
            assert len(self.decks[0]) == len(self.decks[1])
    
    def getIndent(self):
        return "   "*self.id

    def printDecks(self):
        for i in range(self.numPlayers):
            print("Player {}".format(i))
            for card in self.decks[i]:
                print("{} ".format(card),end="")
            print("")
    
    def getHash(self, lst):
        tple = tuple(lst.copy())
        return hash(tple)
    
    def report(self, played):
        indent = self.getIndent()
        print("\n{}ID: {}   -- Round {} --".format(indent,self.id,self.roundNumber))
        print("{}Player 1: {}".format(indent,self.decks[0]))
        print("{}Player 2: {}".format(indent,self.decks[1]))
        print("{}P1: {}".format(indent,played[0]))
        print("{}P2: {}".format(indent,played[1]))

    def checkHistory(self):
        p1ID = self.getHash(self.decks[0])
        p2ID = self.getHash(self.decks[1])
        self.previousDeck1.append(p1ID)
        self.previousDeck2.append(p2ID)
        if p1ID in self.previousDeck1[:-1]:
            #idx = self.previousDeck1.index(p1ID)
            self.gw = 0 # player 1 wins
            #print(str(self.id), " Player 2 lost - repeat deck")
            return True

        if p2ID in self.previousDeck2[:-1]:
            #idx = self.previousDeck2.index(p2ID)
            #self.gw = 0
            return True
        return False
    
    def play(self):
        while True:
            global round_count
            round_count+=1

            if len(self.decks[0]) == 0:
                self.gw = 1
                return 1,self.decks[1]
            elif len(self.decks[1]) == 0:
                self.gw = 0
                return 0,self.decks[0]

            if self.checkHistory():
                self.gw = 0 # player 1 wins

                return 0, None



            if self.VERBOSE:
                print(f"{round_count}:{self.decks[0]}{self.decks[1]}")
            self.roundNumber+=1
            #played = []
            check = []
            #p1ID = self.getHash(self.decks[0])
            #p2ID = self.getHash(self.decks[1])

                
            #for p in range(self.numPlayers):
            card1 = self.decks[0].pop(0)
            card2 = self.decks[1].pop(0)

            #self.report(played)
            if card1 <= len(self.decks[0]) and card2 <= len(self.decks[1]):
                d1 = self.decks[0][:card1].copy()
                d2 = self.decks[1][:card2].copy()
                # check.append(self.getHash(self.decks[0]))
                # check.append(self.getHash(self.decks[1]))
                assert len(d1) == card1
                assert len(d2) == card2
                newDeck = [d1, d2]
                #before = len(self.previousDeck1)
                ng = Game(newDeck, self.id+1)
                gw,wd = ng.play()
                print("")
                #assert len(self.previousDeck1) == before
                assert ng.id == self.id+1
                assert ng.gw == gw
                # if check[0] != self.getHash(self.decks[0]) or check[1] != self.getHash(self.decks[1]):
                #     print("Deck recurrsion error")
                #     exit(1)
                #print("{}{}Player {} Won subgame, claims {}".format(self.id,self.getIndent(),ng.gw,played))
                if ng.gw != 0 and ng.gw != 1:
                    print(str(self.id), "sub game error, no winner found")
                    exit(0)

                if gw == 0:
                    self.decks[0].append(card1)
                    self.decks[0].append(card2)
                else:
                    self.decks[1].append(card2)
                    self.decks[1].append(card1)
                
            else:
                if card1 > card2:
                    self.decks[0].append(card1)
                    self.decks[0].append(card2)
                else:
                    self.decks[1].append(card2)
                    self.decks[1].append(card1)






            if round_count > 10000 and self.id == 0:
                exit(0)
            


    def calculateScore(self):
        winnerDeck = self.decks[self.gw]
        # allcards = self.origDecks[0]
        # allcards.extend(self.origDecks[1])
        # check =  set(allcards).intersection(set(winnerDeck))
        # assert len(check) == 50
        total = 0
        
        # self.printDecks()
        for i, item in enumerate(winnerDeck):
            total += (i+1)*item
            print(f"{i+1}*{item} {total}")
        # while len() > 0:
        #     card = int(winnerDeck.pop())
        #     sum = card * count
        #     total += sum
        #     print ("{} * {} = {}  {}".format(card,count,sum,total))
        #     count+=1
        print("Total Score for Player {} was {}".format(self.gw,total))

    # def playGame(self):
    #     while self.round():
    #         pass
    #     #self.calculateScore()


def hashTest():
    lst = [33, 10, 36, 27, 31, 2, 19, 9, 38, 15, 30, 23]
    lst1 = [33, 10, 36, 27, 31, 2, 19, 9, 38, 15, 30, 23]
    lst2 = [6,7,8,9]
    lst3 = [6,7,8,5]

    tple = tuple(lst)
    tple1 = tuple(lst1)
    tple2 = tuple(lst2)
    tple3 = tuple(lst3)
    h1 = hash(tple)
    h2 = hash(tple1)
    h3 = hash(tple2)
    h4 = hash(tple3)
    if h1 == h2 and (h1 != h3) and (h1 != h4):
        return True
    return False


if hashTest() == False:
    print("hash fail")
    exit(1)


player = -1
deck = None
decks = []
for line in data:
    if "Player" in line:
        player += 1
        if deck is not None:
            decks.append(deck)                
        deck = []
    elif line != "":
        card = int(line)
        deck.append(card)
if deck is not None:
    decks.append(deck)   
#self.numPlayers = player+1
g = Game(decks,0)
g.play()
g.calculateScore()
print(round_count)
# g.round()
# g.printDecks()

        