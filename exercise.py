#!/usr/bin/env python2
# -.- coding: utf-8 -.-
import ui
import settings
from utils import *
import sys
class Exercise(ObjDict):
    def __init__(self, uicurses=None, dic_data=None):
        if uicurses == None:
            self.uicurses = ui.UICurses()
            uicurses=self.uicurses
        else:
            self.uicurses = uicurses
        settings.load_props()
        if not (dic_data is None):
            self.update(dic_data)
        else:
            self.update(settings.core_settings)
        if "required" in self:
            flag, msg = self.check_required()
            if not flag:
                self.uicurses.add_str(msg, 0, 0)
                self.uicurses.wait_any_key(None)
                self.quit()
    
    def check_required(self):
        for item in self.required:
            if item not in self:
                return (False, str(item) + " missing")
        return (True, None)

    def quit(self):
        self.uicurses.quit()
        sys.exit(0)
