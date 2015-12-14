#!/usr/bin/env python2
# -.- coding: utf-8 -.-

import time
import random
import sys
import settings
from exercise import Exercise
import locale
import subprocess
import os
from utils import *

class Reader(Exercise):
    def __init__(self, uicurses=None, dic_data=None):
        self.required = ["text", "BPM", "words"] 
        Exercise.__init__(self, uicurses, dic_data)
        if "encoding" not in self:
            self.encoding=locale.getpreferredencoding()
    
    def get_data(self, text):
        if text=="random":
            if settings.PROGRAM_DIR=="":
                selectedtext="example_text/%02d.txt" % (random.randint(0, 300))  
            else:
                selectedtext = settings.PROGRAM_DIR + "/example_text/%02d.txt" % (random.randint(0, 300))  
            with open(selectedtext, "rb") as fhandle:
                data = fhandle.read()
                data = data.decode("latin_1").encode("utf-8")
        elif self.text=="clipboard":
            data=subprocess.check_output(["/usr/bin/xsel" ,"-o", "-b"]) 
        else:
            if os.access(text, os.R_OK):
                with open(text, "rb") as fhandle:
                    data = fhandle.read()
            else:
                uicurses.add_str("Not text found")
                uicurses.wait_any_key(None)
                self.quit()
        if "encoding" in self:
            if self.encoding == "latin_1":
                data = data.decode("latin_1").encode("utf-8")
        return data

    def sequence_text(self, slicedtext, bpm):
        for text in slicedtext:
            yield text
            timeout, key = self.uicurses.wait_any_key(int((60.0/bpm - 0.001)*1000))
            if key is not None:
                if key==" ":
                    self.uicurses.wait_any_key(None)
                elif key=="q":
                    self.quit()
                elif key=="w":
                    self.BPM+=5
                    bpm+=5
                    self.show_parameters()
                    time.sleep(0.5)
                elif key=="s" and self.BPM>=5:
                    self.BPM-=5
                    bpm-=5
                    self.show_parameters()
                    time.sleep(0.5)
                elif key=="e":
                    time.sleep(0.5)
                elif key=="r":
                    time.sleep(2)
                

    def show_parameters(self):
        self.uicurses.add_str("BPM: " + str(self.BPM), 0, 0, True)
        self.uicurses.add_str("words: " + str(self.words), 1, 0, True)
        self.uicurses.add_str("text: " + str(self.text), 2, 0, True)
        self.uicurses.add_str("encoding: " + str(self.encoding), 3, 0, True)

class LineReader(Reader):
    def run(self):
        uicurses = self.uicurses
        self.data=self.get_data(self.text)
        self.show_parameters()
        for text in self.sequence_text(slice_text(self.data, self.words), self.BPM):
            uicurses.add_str_center(text,-5,-10, True)

class SecuencialReader(LineReader):
    def __init__(self, uicurses=None, dic_data=None):
        self.required = ["text", "BPM", "words"] 
        Exercise.__init__(self, uicurses, dic_data)
    def run(self):
        uicurses = self.uicurses
        selectedtext = self.text
        self.data=self.get_data()
        self.show_parameters()
        for text in self.sequence_text(slice_text(data, self.words), self.BPM):
            uicurses.add_str(text, None, 5, True)

def main():
    sr = LineReader()
    sr.run()
    sr.quit()

if __name__ == "__main__":
    main()
