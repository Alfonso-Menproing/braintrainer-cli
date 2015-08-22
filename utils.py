#!/usr/bin/env python2
# -.- coding: utf-8 -.-
import random
def get_digits(n=2, max_digit=9):
    res=[]
    for _ in range(n):
        res.append(random.randint(0,max_digit))
    return "".join(map(str, res))

