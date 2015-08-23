#!/usr/bin/env python2
# -.- coding: utf-8 -.-
HORIZONTAL = 0
VERTICAL = 1
CIRCLE=0
TRIANGLE=3
SQUARE=4
PENTAGONE=5
HEXAGONE=6
HEPTAGONE=7
OCTAGONE=8
STAR=9
FIGURES=[0,3,4,5,6,7,8,9]

class FiguresDraw:
    def __init__(uicurses):
        self.uicurses = uicurses;
        curses.init_color(1, 800, 500, 500)

    def addfigure(fig):
        if fig==CIRCLE:
            pass
        elif fig==TRIANGLE:
            pass
        elif fig==SQUARE:
            pass
        elif fig==PENTAGONE:
            pass
        elif fig==HEXAGONE:
            pass
        elif fig==HEPTAGONE:
            pass
        elif fig==OCTAGONE:
            pass
        elif fig==STAR:
            pass

