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
    def __init__(self,data):
        self.decks = []
        player = -1
        deck = None
        self.gw = -1
        for line in data:
            #match = re.match(r"Player (\d+):")
            if "Player" in line:
                player += 1
                if deck is not None:
                    self.decks.append(deck)                
                deck = []
            elif line != "":
                card = int(line)
                deck.append(card)
        if deck is not None:
            self.decks.append(deck)   
        self.numPlayers = player+1

    def printDecks(self):
        for i in range(self.numPlayers):
            print("Player {}".format(i))
            for card in self.decks[i]:
                print(card)
    
    def round(self):
        played = []
        for p in range(self.numPlayers):
            played.append(self.decks[p].pop(0))
        winner = played.index(max(played))
        played.sort(reverse=True)
        print("winner: {}".format(winner))
        self.decks[winner].extend(played)

        for p in range(self.numPlayers):
            if len(self.decks[p]) == 0:
                print("Player {} lost".format(p))
                if p == 0:
                    self.gw = 1
                else:
                    self.gw = 0
                return False
        return True

    def calculateScore(self):
        total = 0
        count = 1
        while len(self.decks[self.gw]) > 0:
            card = self.decks[self.gw].pop()
            sum = card * count
            total += sum
            print ("{} * {} = {}  {}".format(card,count,sum,total))
            count+=1
        print("Total Score for Player {} was {}".format(self.gw,total))

    def playGame(self):
        while self.round():
            pass
        self.calculateScore()



            

g = Game(data)
g.playGame()
# g.round()
# g.printDecks()

        