#!/usr/bin/env python2
# -.- coding: utf-8 -.-

import time
import random
import settings
WORD_MEAN_SIZE = 4
MAXLINESIZE = 30

def sliceText(text, words):
    lastindex = 0
    index = 0
    while index < len(text):    
        index = lastindex + (WORD_MEAN_SIZE + 1) * words
        while index < len(text) and text[index] != " " and text[index] != "\n":
            index += 1
        if index >= len(text):
            yield text[lastindex:]
        else:
            yield text[lastindex:index + 1].replace("\n", "-")
        lastindex = index + 1

def sequenceText(slicedtext, bpm):
    for text in slicedtext:
        yield text
        time.sleep(60.0/bpm - 0.001)

class LineReader:
    def __init__(self,uicurses):
        self.uicurses = uicurses
        uicurses.clear()
        settings.load_props()
        if settings.CHOOSE:
            uicurses.addstr("Elija BPM: ")
            self.BPM = int(uicurses.getstr())
            self.words = 3
        else:
            self.BPM = int(settings.get_prop("BPM"))
            self.words = 3

    def run(self):
        uicurses = self.uicurses
        if settings.PROGRAM_DIR=="":
            selectedtext="example_text/%02d.txt" % (random.randint(0, 300))  
        else:
            selectedtext = settings.PROGRAM_DIR + "/example_text/%02d.txt" % (random.randint(0, 300))  
        uicurses.addstr("BPM: " + str(self.BPM))
        uicurses.addstr("words: " + str(self.words))
        with open(selectedtext, "r") as fhandle:
            data = fhandle.read()
        for text in sequenceText(sliceText(data, self.words), self.BPM):
            if len(text) < MAXLINESIZE:
                text=text+" "*(MAXLINESIZE-len(text))
            uicurses.addstr(text,0,5,5,False)

class SecuencialReader:
    def __init__(self,uicurses):
        self.uicurses = uicurses
        uicurses.clear()
        settings.load_props()
        if settings.CHOOSE:
            uicurses.addstr("Elija BPM: ")
            self.BPM = int(uicurses.getstr())
            uicurses.addstr("Elija words:")
            self.words = int(uicurses.getstr())
        else:
            self.BPM = int(settings.get_prop("BPM"))
            self.words = 3

    def run(self):
        uicurses = self.uicurses
        if settings.PROGRAM_DIR=="":
            selectedtext="example_text/%02d.txt" % (random.randint(0, 300))  
        else:
            selectedtext = settings.PROGRAM_DIR + "/example_text/%02d.txt" % (random.randint(0, 300))  
        uicurses.addstr("BPM: " + str(self.BPM))
        uicurses.addstr("words: " + str(self.words))
        with open(selectedtext, "r") as fhandle:
            data = fhandle.read()
        for text in sequenceText(sliceText(data, self.words), self.BPM):
            if len(text) < MAXLINESIZE:
                text=text+" "*(len(text)-MAXLINESIZE)
            uicurses.addstr(text)
