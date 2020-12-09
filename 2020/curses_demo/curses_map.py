import time
import curses
import pickle
import os


#class MapData():
    


class MapLoader():
    PREFERRED_PICKLE_PROTOCOL = 0
    S_FILENAME = ""
    def __init__(self, s_filename):
        self.S_FILENAME = s_filename
        

    def save(self, o_map):
        self.save_obj(o_map, self.S_FILENAME)

    def load(self):
        return self.load_obj(self.S_FILENAME)
            
    def load_obj(self, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

    def save_obj(self, obj, name ):
        with open(name, 'wb') as f:
            pickle.dump(obj, f, self.PREFERRED_PICKLE_PROTOCOL)

class MapViewer():
    NAME = ""

    def __init__(self, x_size, y_size):
        self.debug=True
        self.width = x_size
        self.height = y_size
    

    def draw(self):
        stdscr = curses.initscr()
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak() # don't require enter key
        stdscr.keypad(True)

        y=5
        x=5
        stdscr.addstr(y,x,self.NAME)
        stdscr.refresh()
        time.sleep(3)


        #cleanup before exit
        curses.curs_set(1)
        curses.echo()
        curses.nocbreak()
        stdscr.keypad(False)
        curses.endwin()

    def setName(self,name):
        self.NAME = name

treasure = MapViewer(10,10)
treasure.setName("Treasure!")
treasure.draw()
loader = MapLoader(os.path.join(os.getcwd() + "map.pkl"))
loader.save(treasure)

t2 = loader.load()
t2.setName("More Treasure!")
#print(t2)
t2.draw()

