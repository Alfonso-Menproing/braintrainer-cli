#!/usr/bin/env python2
# -.- coding: utf-8 -.-
import ui
import time
import timemanager
from utils import *
import settings
import exercise

class SecuencialDec(exercise.Exercise):
    def __init__(self, uicurses=None, dic_data=None):
        self.required=["duration", "BPM"]
        exercise.Exercise.__init__(self, uicurses, dic_data)
    def run(self):
        uicurses = self.uicurses
        timemanager.tick()
        uicurses.add_str("BPM: " + str(self.BPM))
        uicurses.add_str("duration: " + str(self.duration))
        while timemanager.tock() < self.duration*1000:
            uicurses.add_str_center(get_digits(),-5,-10)
            time.sleep(60.0 / self.BPM - 0.001)
        settings.send_data({"action" : "check"})

def main():
    ex=SecuencialDec()
    ex.run()
    ex.uicurses.quit()

if __name__ == "__main__":
    main()
