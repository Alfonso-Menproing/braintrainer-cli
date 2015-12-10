#!/usr/bin/env python2
# -.- coding: utf-8 -.-
import random
import sys

def split_string(string, space): 
    res = []
    newstring = string
    while len(newstring) > space:
        res.append(newstring[0:space])
        newstring = newstring[space:]
    if len(newstring) > 0:
        res.append(newstring)
    return res

def get_digits(n=2, max_digit=9):
    res=[]
    for _ in range(n):
        res.append(random.randint(0,max_digit))
    return "".join(map(str, res))

def parse_argv():
    result = {}
    for item in sys.argv[1:]:
        key, value = item.split("=")
        try:
            result[key]=int(value)
        except:
            try:
                result[key]=float(value)
            except:
                result[key]=value
    return result        
class ObjDict(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)

def main():
    """ testing split string """
    print(str(split_string("example string", 3)))


if __name__ == "__main__":
    main()
