import json
from colorama import Fore, Back, Style, init
import os
import re
import common.util as util
import time

from datetime import timezone, datetime


dt = datetime(2022, 1, 1)
FUTURE_TIME = dt.replace(tzinfo=timezone.utc).timestamp()
BOTH = 4
GOLD = 2
SILVER = 1


class Users:
    def __init__(self, file):
        self.users = []
        self.data = util.readfile(file)
        self.sfinish = []
        self.gfinish = []
        self.udict = {}

        self.load()

    def load(self):
        parsed = json.loads(self.data[0])['members']
        for key in parsed:
        #   print("key {} value: {}".format(key, parsed[key]['name']))
            self.users.append(User(parsed[key]))
        self.users.sort(key=lambda x: x.local_score, reverse=True)
        for u in self.users:
            self.udict[u.id] = u

    def print_users(self):
        for u in self.users:
            print("{: <30} score: {: <4} ".format(u.name, u.local_score), end="")
            u.CompletionLevel.getStarString()

    def printFinishOrder(self):
        print("{: <30} | {: <6} ".format("Name", "Score"), end="")
        for i in range(1,26):
            print("|  {:02d}   ".format(i),end="")
        print("|")
        print("-"*241)
        for u in self.users:
            print("{: <30} | {: <6} ".format(u.name, u.local_score), end="")
            for d in range(0,25):
                s = u.getPlace(d, SILVER)
                g = u.getPlace(d, GOLD)
                if s == 0:
                    ss = "--"
                else:
                    ss = "{:02d}".format(s)

                if g == 0:
                    gg = "--"
                else:
                    gg = "{:02d}".format(g)

                
                print("| {} {} ".format(ss,gg), end="")
            print("|")
        #for u in self.users:

    # def getPlace(self,day,star,id):
    #     return self.timestamps[day][star-1]

    def getUser(self,id):
        return self.udict[id]


    def findFinishes(self):
        self.timestamps = []
        for d in range(0,25):
            ts = []
            for u in self.users:
                user_ts = u.getTimeStamps(d+1)
                if user_ts:
                    ts.append(user_ts)
            self.timestamps.append(ts)
        for d in range(0,25):
            self.timestamps[d].sort(key=lambda x: x[1], reverse=False)
            #print(self.timestamps[d])
            place = 0
            for i in self.timestamps[d]:
                if i[1] < FUTURE_TIME and i[1] > 0:
                    place+=1
                    u = self.getUser(i[0])
                    #print("{} {}".format(u.name,place))
                    u.setPlace(d,SILVER,place)
            place = 0
            self.timestamps[d].sort(key=lambda x: x[2], reverse=False)
            for i in self.timestamps[d]:
                if i[2] < FUTURE_TIME and i[2] > 0:
                    place+=1
                    u = self.getUser(i[0])
                    #print("{} {}".format(u.name,place))
                    u.setPlace(d,GOLD,place)
        
    def printPlaces(self,day,star):
            for u in self.users:
                print("{} : {}".format(u.name,u.getPlace(day,star)))

        #print(self.timestamps)
    
    def printDayReport(self,day, star):
        table = []
        for u in self.users:
            ts = u.getTimeStamps(day)
            if ts[SILVER] == FUTURE_TIME and ts[GOLD] == FUTURE_TIME:
                continue

            if ts[1] == FUTURE_TIME or ts[1] == 0:
                t1 = "-------------------" 
                     
            else:
                t1 = datetime.fromtimestamp(ts[SILVER])
            
            if ts[2] == FUTURE_TIME or ts[2] == 0:
                t2 = "-------------------"
            else:
                t2 = datetime.fromtimestamp(ts[GOLD])

            if star == BOTH:
                table.append((u.name,ts[SILVER], t1 , t2))
            else:
                table.append((u.name,ts[GOLD], t1, t2))
        table.sort(key=lambda x: x[1])
        for i in table:
            if star == BOTH:
                print("{: <30} {}    {}".format(i[0], i[2], i[3]))
            else:
                print("{: <30} {}".format(i[0], i[2]))




class User:
    # "name":"boilermaker__2015",
    # "id":"709770",
	# "global_score":0,
	# "local_score":164,
	# "last_star_ts":"1607446154",
	# "stars":15,
    def __init__(self, data):
        self.name = data['name']
        self.id = data['id']
        self.global_score = data['global_score']
        self.local_score = data['local_score']
        self.last_star_ts = data['last_star_ts']
        self.stars = data['stars']
        self.CompletionLevel = Completion( data['completion_day_level'])
        self.gplaces = [0]*25
        self.splaces = [0]*25
    
    def getTimeStamps(self,day):
        ts = self.CompletionLevel.getTimeStamps(day)
        return (self.id, ts[0],ts[1])

    
    def setPlace(self,day, star, place):
        if star == GOLD:
            self.gplaces[day] = place
        elif star == SILVER:
            self.splaces[day] = place

    def getPlace(self,day,star):
        if star == GOLD:
            return self.gplaces[day]
        elif star == SILVER:
            return self.splaces[day]
        return -1


class Completion:
    def __init__(self,data):
        self.days = []

        for day in data:
            s_ts = 0
            g_ts = 0
            if '1' in data[day]:
                if 'get_star_ts' in data[day]['1']:
                    s_ts = int(data[day]['1']['get_star_ts'])
            if '2' in data[day]:
                if 'get_star_ts' in data[day]['2']:
                    g_ts = int(data[day]['2']['get_star_ts'])

            self.days.append(Days(day, s_ts, g_ts))

    def timestamps(self):
        for d in self.days:
            print("{}: {},{}".format(d.day, d.silver_ts,d.gold_ts))

    def getStarString(self):
        for i in range(1,26):
            found = False
            for d in self.days:
                if int(d.day) == i:    
                    found = True
                    if d.gold_ts != 0:
                        print(Fore.YELLOW + "*", end="")
                    elif d.silver_ts != 0:
                        print(Style.BRIGHT + Fore.WHITE + "+", end="")
                    else:
                        print(Fore.BLUE + " ", end="")
            if not found:
                print(Fore.BLUE + " ", end="")
        print("")

    def getTimeStamps(self,day):
        for d in self.days:
            if int(d.day) == day:
                return (d.silver_ts,d.gold_ts)
        return (FUTURE_TIME,FUTURE_TIME)

class Days:
    def __init__(self,day,s_ts,g_ts):
        self.day = day
        self.silver_ts = s_ts
        self.gold_ts = g_ts



init(autoreset=True)
users = Users(util.AOC_2020 + "\\JSON\\data.json")
users.print_users()
#users.printFinishOrder()
users.findFinishes()
#users.printPlaces(1, SILVER)
users.printFinishOrder()
users.printDayReport(10, BOTH)
