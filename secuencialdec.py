#!/usr/bin/env python2
# -.- coding: utf-8 -.-
import ui
import time
import timemanager
from utils import *
import settings

class SecuencialDec:
    def __init__(self, uicurses):
        self.uicurses = uicurses
        settings.load_props()
        if settings.CHOOSE:
            uicurses.addstr("Elija BPM: ")
            self.BPM=int(uicurses.getstr())
            uicurses.addstr("Elija duration: ")
            self.duration=int(uicurses.getstr())
            uicurses.clear()
        else:
            self.BPM = int(settings.get_prop("BPM"))
            self.duration = int(settings.get_prop("duration"))

    def run(self):
        uicurses = self.uicurses
        timemanager.tick()
        uicurses.addstr("BPM: " + str(self.BPM))
        uicurses.addstr("duration: " + str(self.duration))
        while timemanager.tock() < self.duration:
            uicurses.addstrcenter(get_digits(),0,-5,-10)
            time.sleep(60.0 / self.BPM - 0.001)
        settings.check()
