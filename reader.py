#!/usr/bin/env python2
# -.- coding: utf-8 -.-

import time
import random
import settings
import exercise
import locale
import subprocess
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
            yield text[lastindex:].replace("\n"," \\")
        else:
            yield text[lastindex:index + 1].replace("\n", " \\")
        lastindex = index + 1

def sequenceText(slicedtext, bpm):
    for text in slicedtext:
        yield text
        time.sleep(60.0/bpm - 0.001)

class LineReader(exercise.Exercise):
    def run(self):
        uicurses = self.uicurses
        selectedtext = self.text
        if self.text=="random":
            if settings.PROGRAM_DIR=="":
                selectedtext="example_text/%02d.txt" % (random.randint(0, 300))  
            else:
                selectedtext = settings.PROGRAM_DIR + "/example_text/%02d.txt" % (random.randint(0, 300))  
            with open(selectedtext, "rb") as fhandle:
                self.data = fhandle.read()
                self.data = self.data.decode("latin_1").encode("utf-8")
        elif self.text=="clipboard":
            self.data=subprocess.check_output(["/usr/bin/xsel" ,"-o", "-b"]) 
        else:
            with open(selectedtext, "rb") as fhandle:
                self.data = fhandle.read()
        if "encoding" in self:
            if self.encoding == "latin_1":
                self.data = self.data.decode("latin_1").encode("utf-8")
        else:
            self.encoding=locale.getpreferredencoding()

        uicurses.add_str("BPM: " + str(self.BPM))
        uicurses.add_str("words: " + str(self.words))
        uicurses.add_str("text: " + str(selectedtext))
        uicurses.add_str("encoding: " + str(self.encoding))
        for text in sequenceText(sliceText(self.data, self.words), self.BPM):
            uicurses.add_str_center(text,-5,-10, True)

class SecuencialReader(exercise.Exercise):
    def run(self):
        uicurses = self.uicurses
        if settings.PROGRAM_DIR=="":
            selectedtext="example_text/%02d.txt" % (random.randint(0, 300))  
        else:
            selectedtext = settings.PROGRAM_DIR + "/example_text/%02d.txt" % (random.randint(0, 300))  
        uicurses.add_str("BPM: " + str(self.BPM))
        uicurses.add_str("words: " + str(self.words))
        uicurses.add_str("file: " + str(selectedtext))
        uicurses.add_str("encoding: " + str(locale.getpreferredencoding()))
        with open(selectedtext, "r") as fhandle:
            data = fhandle.read()
            data = data.decode("latin_1").encode("utf-8")
        for text in sequenceText(sliceText(data, self.words), self.BPM):
            uicurses.add_str(text, None, 5, True)

def main():
    sr = LineReader()
    sr.run()
    sr.quit()

if __name__ == "__main__":
    main()
