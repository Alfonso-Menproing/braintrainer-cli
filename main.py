#!/usr/bin/env python2
# -.- coding: utf-8 -.-
import ui
import table
import time
import settings
def main():
    uicurses = ui.UICurses() 
    choosing_i=0
    while True:
        uicurses.clear()
        choosing_list = [key for key in table.exercises_list] + ["Quit"]
        choosing_i = uicurses.select(choosing_list,None,0,choosing_i)
        choosen = choosing_list[choosing_i]
        if choosen=="Quit":
            break
        exercise = table.exercises_list[choosen](uicurses, table.default_config[choosen])
        exercise.run()
    uicurses.quit()

if __name__ == "__main__":
    main()
