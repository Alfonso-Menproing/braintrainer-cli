#!/usr/bin/env python2
# -.- coding: utf-8 -.-
import curses
import time
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
        self.lines = [0]
        self.win.clear()
        self.ymax, self.xmax=self.win.getmaxyx()
        self.children = [self.win]
        self.newliney,self.newlinex = (0,5)
        self.clearifnewline = True
        self.lastkeys=[0,0,0]

    def setnewlinex(val):
        self.newlinex = val

    def setnewliney(val):
        self.newliney = val

    def addwin(self,nline,ncol,y, x):
        new_win = self.win.derwin(nline,ncol,y,x)
        new_win.nodelay(1)
        self.children.append(new_win)
        self.lines.append(0)

    def setline(self,val,child=0):
        self.lines[child] = val

    def addstr(self, string, child=0,y=None,x=0, newline=True):
        if y is None:
            y=self.lines[child]
        if y>=self.ymax:
            y=self.newliney
            self.lines[child]=y
            newline=True
            if self.clearifnewline:
                self.clear(child)
        if x + len(string)>=self.xmax:
            firstpart = string[0:self.xmax-1]
            secondpart = string[self.xmax-1:]
            self.addstrrel(firstpart,child,y,x)
            self.addstr(secondpart,child,y + 1,self.newlinex,newline)
        else:
            self.children[child].addstr(y, x, string)
            if newline:
                self.lines[child] = y + 1
            self.children[child].refresh()

    def addstrrel(self,string,child=0,y=0,x=0):
        y=self.lines[child] + y
        self.children[child].addstr(y, x, string)
        self.children[child].refresh()

    def addstrcenter(self, string, child=0, y=0, x=0):
        self.addstr(string, child, self.ymax/2+y, self.xmax/2+x)

    def clear(self,child=0):
        self.children[child].clear()
        self.setline(0)

    def getstr(self,child=0):
        curses.echo()
        curses.nocbreak()
        self.win.nodelay(0)
        res = self.children[child].getstr(self.lines[child], 0)
        self.lines[child] += 1
        self.win.nodelay(1)
        curses.noecho()
        curses.cbreak()
        return res

    def select(self, cat, child=0, y=None,x=0,defaultfocus=0, orientation=HORIZONTAL):
        newline=True
        if y is None:
            y=self.lines[child]
        if orientation==HORIZONTAL:
            nextline = y + 1
        elif orientation==VERTICAL:
            nextline = y + len(cat)
        cat_list=list(cat)
        focus = defaultfocus
        cat_list[focus]=cat_list[focus].upper()
        if orientation==HORIZONTAL: 
            self.addstr(" ".join(cat_list), child,y, x)
        elif orientation==VERTICAL:
            for item_i,item in enumerate(cat_list):
                self.addstr(str(item), child,y + item_i, x,False)
        self.children[child].refresh()
        while True:
            c=self.win.getch()
            self.push_key(c)
            if c>-1 and c<256:
                if self.is_key_enter():
                    if newline:
                        self.lines[child] += nextline
                    return focus

                elif chr(c)=='l' or self.is_key_right():
                    cat_list[focus]=cat_list[focus].lower()
                    focus=(focus + 1) % len(cat_list)
                    cat_list[focus]=cat_list[focus].upper()
                    if orientation==HORIZONTAL: 
                        self.addstr(" ".join(cat_list), child,y, x)
                    elif orientation==VERTICAL:
                        for item_i,item in enumerate(cat_list):
                            self.addstr(str(item), child,y + item_i, x,False)
                    self.children[child].refresh()
                elif chr(c)=='h' or self.is_key_left():
                    cat_list[focus]=cat_list[focus].lower()
                    focus=(focus - 1) % len(cat_list)
                    cat_list[focus]=cat_list[focus].upper()
                    if orientation==HORIZONTAL: 
                        self.addstr(" ".join(cat_list), child,y, x)
                    elif orientation==VERTICAL:
                        for item_i,item in enumerate(cat_list):
                            self.addstr(str(item), child,y + item_i, x,False)
                    self.children[child].refresh()
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

    def quit(self):
        curses.endwin()

def main():
    uicurses=UICurses()
    curses.nocbreak()
    while True:
        time.sleep(1)
        uicurses.addstr(str(uicurses.win.getch()))


if __name__ == "__main__":
    main()
