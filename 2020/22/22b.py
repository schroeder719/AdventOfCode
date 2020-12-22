import os
import re
import common.util as u
#import common.comp as c
import logging
import time
import copy
import math
import queue


#data = u.readfile(u.AOC_2020 + "\\22\\input_ex.txt")
data = u.readfile(u.AOC_2020 + "\\22\\input.txt")

class Game:
    def __init__(self,decks,id):
        self.previousDecks = []
        self.decks = []
        self.gw = -1
        self.decks = decks
        self.numPlayers = len(decks)
        self.id = id

    def printDecks(self):
        for i in range(self.numPlayers):
            print("Player {}".format(i))
            for card in self.decks[i]:
                print(card)
    
    def getHash(self, lst):
        tple = tuple(lst)
        return hash(tple)
    
    def report(self):
        print("ID: {}".format(self.id))
        print("Player 1: {}".format(self.decks[0]))
        print("Player 2: {}".format(self.decks[1]))
    
    def round(self):
        played = []
        p1ID = self.getHash(self.decks[0])
        p2ID = self.getHash(self.decks[1])
        self.report()

        if p1ID in self.previousDecks or p2ID in self.previousDecks:
            self.gw = 1
            print(str(self.id), " Player 2 lost - repeat deck")
            return False
        else:
            self.previousDecks.extend([p1ID,p2ID])
            
        for p in range(self.numPlayers):
            played.append(self.decks[p].pop(0))
        if played[0] <= len(self.decks[0]) and played[1] <= len(self.decks[1]):
            d1 = (self.decks[0][:played[0]]).copy()
            d2 = (self.decks[1][:played[1]]).copy()
            newDeck = [d1,d2 ]
            ng = Game(newDeck, self.id+1)
            ng.playGame()
            if ng.gw == 0: 
                print(str(self.id), "Player 2 Lost subgame")
            elif ng.gw == 1:
                print(str(self.id), "Player 1 Lost subgame")
            else:
                print(str(self.id), "sub game error, no winner found")
                exit(0)
            first  = played.pop(ng.gw)
            second = played.pop()
            self.decks[ng.gw].extend([first,second])
        else:
            winner = played.index(max(played))
            played.sort(reverse=True)
            print(str(self.id), "winner: {}".format(winner))
            self.decks[winner].extend(played)

        for p in range(self.numPlayers):
            if len(self.decks[p]) == 0:
                print(str(self.id), "Player {} lost".format(p))
                if p == 0:
                    self.gw = 1
                else:
                    self.gw = 0
                return False
        return True

    def calculateScore(self):
        total = 0
        count = 1
        winnerDeck = self.decks[self.gw]
        while len(winnerDeck) > 0:
            card = int(winnerDeck.pop())
            sum = card * count
            total += sum
            print ("{} * {} = {}  {}".format(card,count,sum,total))
            count+=1
        print("Total Score for Player {} was {}".format(self.gw,total))

    def playGame(self):
        while self.round():
            pass
        #self.calculateScore()


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
g.playGame()
g.calculateScore()
# g.round()
# g.printDecks()

        