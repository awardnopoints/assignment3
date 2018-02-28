#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 09:36:01 2018

@author: eoin
"""

import light as l
import sys
import re
import os
import urllib.request

def main():
    if len(sys.argv) < 2:
        sys.exit("Must give filename/location or URL as first argument.")
    target = sys.argv[1]
    print(target[0:7])
    if target[0:7] == 'http://':
        with urllib.request.urlopen(target) as response, open("tempinput.txt", 'wb') as out_file:
            data = response.read()
            out_file.write(data)
            myfile = open("tempinput.txt", 'r')
    else:
        myfile = open(target, 'r')
    print(myfile)
    lines = list(myfile)
    print(lines[0:5])
    L = int(lines[0])
    myLight = l.Light(L)
    for i in range(1, len(lines)):
        obey(lines[i], myLight)
    print(myLight.count())
    if os.path.isfile("tempinput.txt"):
        os.remove("tempinput.txt")
        
def obey(command, light):
    c = regexInterpret(command)
    if c[0]:
        if c[1] == "turn on":
            light.on(int(c[2]), int(c[3]), int(c[4]), int(c[5]))
        elif c[1] == "turn off":
            light.off(int(c[2]), int(c[3]), int(c[4]), int(c[5]))
        elif c[1] == "switch":
            light.switch(int(c[2]), int(c[3]), int(c[4]), int(c[5]))

def regexInterpret(c):
    result = []
    p = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    m = p.match(c)
    if m is None:
        return [False]
    else:
        result.append(True)
        for i in m.groups():
            result.append(i)
        return result
    
    
if __name__ == '__main__':
    main()