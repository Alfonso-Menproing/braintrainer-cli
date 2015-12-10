#!/usr/bin/env python2
# -.- coding: utf-8 -.-
import ui
import settings
from utils import *
import sys
class Exercise(ObjDict):
    def __init__(self, uicurses=None):
        if uicurses == None:
            self.uicurses = ui.UICurses()
            uicurses=self.uicurses
        else:
            self.uicurses = uicurses
        settings.load_props()
        self.update(settings.core_settings)
    def quit(self):
        self.uicurses.quit()
        sys.exit(0)
