import json
from colorama import Fore, Back, Style, init
import os
import re
import common.util as util
import time
import requests

from datetime import timezone, datetime
import browser_cookie3 as bc3
import bs4
import os
from os import path

import plotly.express as px
import plotly.graph_objects as go
#import numpy as np



dt = datetime(2022, 1, 1)
FUTURE_TIME = dt.replace(tzinfo=timezone.utc).timestamp()

st = datetime(2020, 12, 1)
START_TIME = st.replace(tzinfo=timezone.utc).timestamp()
BOTH = 4
GOLD = 2
SILVER = 1



class Data:
    url_json = 'https://adventofcode.com/2020/leaderboard/private/view/614401.json'
    datefile = util.AOC_COMMON + '/Leaderboard/timestamp'
    sessionfile = util.AOC_COMMON + '/Leaderboard/session'
    jsonfile = util.AOC_COMMON + '/Leaderboard/data.json'
    imagefolder = util.AOC_COMMON + '/Leaderboard/images/'
    min_elapsed_time = 900.0
    
    def __init__(self):
        self.session = {}
        self.checkStoredDate()
        if not os.path.exists(self.imagefolder):
            os.mkdir(self.imagefolder)
        
    def getDateFromFile(self):
        try:
            stored_time = datetime.fromtimestamp(float(self.getFromFile(self.datefile)))
            return stored_time
        except:
            return None
    

    def getDateString(self, fmt="%m/%d/%Y, %H:%M:%S"):
        dt = self.getDateFromFile()
        if dt:
            return dt.strftime(fmt)
        else:
            return None



    def checkStoredDate(self):
        date_good = True
        if os.path.exists(self.datefile):
            stored_time = self.getDateFromFile()
            if stored_time:
                now = datetime.now()
                delta = now - stored_time
                #print(delta.total_seconds())
                if delta.total_seconds() > self.min_elapsed_time:
                    date_good = False
            else:
                date_good = False
        else:
            date_good = False
        if not date_good:
            self.getJSON()

    def updateStoredDate(self):
        dt = datetime.now()
        self.saveToFile(self.datefile,"{}".format(dt.timestamp()))

    def getSessionCookie(self):
        if self.getSessionCookieFromFile():
            return True
        else:
            return self.getSessionCookieFromChrome()
        
    def getSessionCookieFromFile(self):
        session = self.getFromFile(self.sessionfile)
        if session:
            self.session = json.loads(session)
            return True
        else:
            return self.getSessionCookieFromChrome()
        
    def getSessionCookieFromChrome(self):
        def get_owner(token):
            """parse owner of the token. returns None if the token is expired/invalid"""
            url = "https://adventofcode.com/settings"
            response = requests.get(url, cookies={"session": token}, allow_redirects=False)
            if response.status_code != 200:
                # bad tokens will 302 redirect to main page
            # log.info("session %s is dead - status_code=%s", token, response.status_code)
                return None
            result = "unknown/unknown"
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            for span in soup.find_all("span"):
                if span.text.startswith("Link to "):
                    auth_source = span.text[8:]
                    auth_source = auth_source.replace("https://twitter.com/", "twitter/")
                    auth_source = auth_source.replace("https://github.com/", "github/")
                    auth_source = auth_source.replace("https://www.reddit.com/u/", "reddit/")
                    #log.debug("found %r", span.text)
                    result = auth_source
                elif span.img is not None:
                    if "googleusercontent.com" in span.img.attrs.get("src", ""):
                        #log.debug("found google user content img, getting google username")
                        result = "google/" + span.text
            return result

        cookie_jar_chrome = bc3.chrome(domain_name=".adventofcode.com")
        chrome = [c for c in cookie_jar_chrome if c.name == "session"]
        #log.info("%d candidates from chrome", len(chrome))
        working = {}
        for cookie in chrome:
            token = cookie.value
            owner = get_owner(token)
            if owner is not None:
                working[token] = owner
        #log.debug("found %d live tokens", len(working))
        for cookie in working.items():
            print("%s <- %s" % cookie)
            self.session = { "session": token }
        self.saveToFile(self.sessionfile,json.dumps(self.session,indent=4))
        return True

    def dateTest(self):
        
        stored_time = datetime.fromtimestamp(float(self.getFromFile(self.datefile)))
    
    def saveToFile(self,file, string):
        with open(file, 'w') as f:
            f.write(string)

    def getFromFile(self,file):
        if not os.path.exists(file):
            return None

        with open(file,'r') as f:
            try:
                read = f.readline().strip()
            except:
                read = None
        return read
        
    def getJSON(self):
        if not self.getSessionCookie():
            print("Failed to get session cookie")
            exit(1)
        
        USER_AGENT = {"User-Agent": "ars v1"}
        r = requests.get(self.url_json, cookies=self.session, headers=USER_AGENT)
        if r.status_code == 200:
            self.saveToFile(self.jsonfile, r.text)
            self.updateStoredDate()
        else:
            print("Error updating JSON")
        

class Users:
    def __init__(self, file):
        self.users = []
        self.data = util.readfile(file)
        self.sfinish = []
        self.gfinish = []
        self.udict = {}
        self.valid_days = []
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

    def printReport(self):
        self.print_users()
        self.findFinishes()
        self.printFinishOrder()
        for d in self.valid_days:
            users.printDayReport(d, BOTH)
            print("")

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
            if place > 0:
                self.valid_days.append(d+1)
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
        print("Day {}".format(day))
        print("-"*75)
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


    def graphFinishes(self,show=True,fileName = None):
        # requires that findFishes be run first
        class GraphData():
            def __init__(self, name):
                self.name = name
                self.starFinishTimes = []
                self.score = []
            def addPoint(self, time, score):
                self.starFinishTimes.append(time)
                self.score.append(score)

        userCount = len(self.users)
        gdl = []
        for u in self.users:
            gd = GraphData(u.name)
            gd.addPoint(datetime.fromtimestamp(START_TIME),0)
            total_score = 0
            for day in self.valid_days:
                s = u.getPlace(day,SILVER)
                g = u.getPlace(day,GOLD)
                ts = u.getTimeStamps(day)
                
                if ts[SILVER] != 0 and ts[SILVER] != FUTURE_TIME:
                    total_score += userCount-s
                    gd.addPoint( datetime.fromtimestamp(ts[SILVER]),total_score)
                    if ts[GOLD] != 0 and ts[GOLD] != FUTURE_TIME:
                        total_score += userCount-g
                        gd.addPoint( datetime.fromtimestamp(ts[GOLD]),total_score)


            gdl.append(gd)
                #ts = u.getTimeStamps(day)
                #t = np.linspace(0, 2*np.pi, 100)
        # for u in gdl:
        #     print("{}: {}".format(u.name,u.score))
        fig = go.Figure()
        for u in gdl:
            fig.add_trace(go.Scatter(x=u.starFinishTimes, y=u.score,
                    mode='lines+markers',
                    name=u.name))
        if fileName:
            fig.write_image(os.path.join(Data.imagefolder,fileName), engine="kaleido", format="png", width=1920, height=1080, scale=1)
        if show:
            fig.show()

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

d = Data()
print("Data was updated: {}".format(d.getDateString()))

init(autoreset=True)
users = Users(util.AOC_COMMON + "\\Leaderboard\\data.json")
users.printReport()
users.graphFinishes(False, fileName="17.png")

