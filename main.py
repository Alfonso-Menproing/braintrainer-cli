#!/usr/bin/env python2
# -.- coding: utf-8 -.-
import ui
import table
import time
import settings
def main():
    uicurses = ui.UICurses() 
    quit = False
    choosing_i=0
    while not quit:
        uicurses.clear()
        uicurses.setline(0)
        choosing_list = [key for key in table.exercises_list]
        choosing_i = uicurses.select(choosing_list,0,None,0,choosing_i)
        exercise = table.exercises_list[choosing_list[choosing_i]](uicurses)
        exercise.run()

if __name__ == "__main__":
    main()
