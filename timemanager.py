#!/usr/bin/env python2
# -.- coding: utf-8 -.-

import time
timedict = {}
timedict["default"]=time.time()
def tick(key="default"):
    timedict[key]=time.time()
def tock(key="default"):
    return time.time()-timedict[key]
def get_week():
    return time.localtime().tm_wday
def get_ymd():
    return time.strftime("%y-%m-%d")
def iterate_ymd():
    current_time=time.localtime()
    current_time=list(current_time)
    current_time[2]-=current_time[6]
    for i in range(7):
        new_time = time.mktime(current_time)
        new_time = time.localtime(new_time)
        yield time.strftime("%y-%m-%d", new_time)
        current_time[2]+=1

def main():
    print(str(list(iterate_ymd())))


if __name__ == "__main__":
    main()

