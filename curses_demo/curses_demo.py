import time
import curses

stdscr = curses.initscr()
curses.curs_set(0)
curses.noecho()
curses.cbreak() # don't require enter key
stdscr.keypad(True)

y=5
x=5
stdscr.addstr(y,x,"Hello")
stdscr.refresh()
time.sleep(3)


#cleanup before exit
curses.curs_set(1)
curses.echo()
curses.nocbreak()
stdscr.keypad(False)
curses.endwin()