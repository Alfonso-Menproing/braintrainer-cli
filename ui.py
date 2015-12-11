#!/usr/bin/env python2
# -.- coding: utf-8 -.-
import curses
import time
from utils import *
import locale
locale.setlocale(locale.LC_ALL, "")
HORIZONTAL=0
VERTICAL=1
class UICurses:
    def __init__(self):
        self.win = curses.initscr()
        curses.start_color()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.win.nodelay(1)
        self.line = 0
        self.win.clear()
        self.ymax, self.xmax=self.win.getmaxyx()
        self.lastkeys=[0,0,0]

    def set_line(self,y):
        self.line = y

    def add_str(self, string, y=None,x=0, blank=False):
        if y is None:
            y=self.line
        for chunk in split_string(string, self.xmax - x):
            self._add_str(chunk, y, x, blank)

    def _add_str(self, string, y=None,x=0, blank=False):
        if x < 0:
            x=0
        if x >= self.xmax:
            x=self.xmax-1
        if y is None:
            y=self.line
        if y<0:
            y=0
        if y>=(self.ymax-1):
            self.clear()
            y=0
        if blank:
            remaining = self.xmax - len(string)
            if remaining > 0:
                string = " "*x + string + " "*remaining
            self.win.addstr(y, 0, string)
        else:
            self.win.addstr(y, x, string)
        self.line = y + 1
        self.win.refresh()

    def grid_add_str(self, string, y, x, ny, nx, blank=True, displacement=0):
        y_chunk = self.ymax / ny
        x_chunk = self.xmax / nx
        y=y*y_chunk
        x=x*x_chunk
        if len(string)>= x_chunk-displacement:
            string=string[:x_chunk-displacement]
        if not blank:
            self.add_str(string, y, x+displacement)
        else:
            self.add_str(string+" "*(len(string)-x_chunk), y, x+displacement)

    def add_str_center(self, string, y=0, x=0, blank=False):
        self.add_str(string, self.ymax/2+y, self.xmax/2-len(string)/2 + x, blank)

    def clear(self):
        self.win.clear()
        self.set_line(0)

    def get_str(self, y=None, x=0):
        if y is None:
            y=self.line
        curses.echo()
        curses.nocbreak()
        self.win.nodelay(0)
        res = self.win.getstr(y, x)
        self.line += 1
        self.win.nodelay(1)
        curses.noecho()
        curses.cbreak()
        return res
    
    def grid_get_str(self, y, x, ny, nx, displacement=0):
        y_chunk = self.ymax / ny
        x_chunk = self.xmax / nx
        y=y*y_chunk
        x=x*x_chunk+displacement
        res=self.get_str(y, x)
        return res

    def select(self, cat, y=None,x=0,defaultfocus=0, orientation=HORIZONTAL):
        self.win.nodelay(0)
        newline=True
        if y is None:
            y=self.line
        if orientation==HORIZONTAL:
            nextline = y + 1
        elif orientation==VERTICAL:
            nextline = y + len(cat)
        cat_list=list(cat)
        focus = defaultfocus
        cat_list[focus]=cat_list[focus].upper()
        if orientation==HORIZONTAL: 
            self.add_str(" ".join(cat_list), y, x)
        elif orientation==VERTICAL:
            for item_i,item in enumerate(cat_list):
                self.add_str(str(item), y + item_i, x)
        self.win.refresh()
        while True:
            c=self.win.getch()
            self.push_key(c)
            if c>-1 and c<256:
                if self.is_key_enter():
                    self.line += nextline
                    self.win.nodelay(1)
                    return focus

                elif chr(c)=='l' or self.is_key_right():
                    cat_list[focus]=cat_list[focus].lower()
                    focus=(focus + 1) % len(cat_list)
                    cat_list[focus]=cat_list[focus].upper()
                    if orientation==HORIZONTAL: 
                        self.add_str(" ".join(cat_list), y, x)
                    elif orientation==VERTICAL:
                        for item_i,item in enumerate(cat_list):
                            self.add_str(str(item), child,y + item_i, x)
                    self.win.refresh()
                elif chr(c)=='h' or self.is_key_left():
                    cat_list[focus]=cat_list[focus].lower()
                    focus=(focus - 1) % len(cat_list)
                    cat_list[focus]=cat_list[focus].upper()
                    if orientation==HORIZONTAL: 
                        self.add_str(" ".join(cat_list), y, x)
                    elif orientation==VERTICAL:
                        for item_i,item in enumerate(cat_list):
                            self.add_str(str(item), y + item_i, x)
                    self.win.refresh()
    def push_key(self, key):
        self.lastkeys[0]=self.lastkeys[1]
        self.lastkeys[1]=self.lastkeys[2]
        self.lastkeys[2]=key

    def is_key_left(self):
        return self.lastkeys==[27,91,68]

    def is_key_right(self):
        return self.lastkeys==[27,91,67]

    def is_key_enter(self):
        return self.lastkeys[2]==10

    def wait_till_key(self, keytostop, timeout_ms):
        init_time_ms = time.time() * 1000
        while (timeout_ms is None) or time.time()*1000 < (init_time_ms + timeout_ms):
            c=self.win.getch()
            self.push_key(c)
            if keytostop=="ENTER" and self.is_key_enter():
                return int(time.time()*1000 - init_time_ms)
            if c > -1 and c < 256 and chr(c)==keytostop:
                return int(time.time()*1000 - init_time_ms)
        return timeout_ms

    def wait_any_key(self, timeout_ms):
        init_time_ms = time.time() * 1000
        while (timeout_ms is None) or time.time()*1000 < (init_time_ms + timeout_ms):
            c=self.win.getch()
            self.push_key(c)
            if self.is_key_enter():
                return (int(time.time()*1000 - init_time_ms), "ENTER")
            if c > -1 and c < 256:
                return (int(time.time()*1000 - init_time_ms),chr(c))
        return (timeout_ms, None)

    def quit(self):
        curses.echo()
        curses.nocbreak()
        curses.endwin()
    
    def add_dict(self, data):
        for key in data:
            self.add_str(str(key) + ": " + str(data[key]))

def main():
    uicurses=UICurses()
    for i in range(3):
        for j in range(3):
            uicurses.grid_add_str(str(i)+str(j),i,j,3,3)
            time.sleep(1)


if __name__ == "__main__":
    main()
