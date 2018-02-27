#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 09:36:01 2018

@author: eoin
"""

import light as l
import sys
import re

def main():
    file = sys.argv[1]
    myfile = open(file, 'r')
    lines = list(myfile)
    L = lines[0]
    myLight = l.Light(L)
    for i in range(1, len(lines)):
        obey(lines[i], myLight)
    print(myLight.count())
        
def obey(command, light):
    c = regexInterpret(command)
    if c[0]:
        if c[1] == "turn on":
            light.on(c[2], c[3], c[4], c[5])
        elif c[1] == "turn off":
            light.off(c[2], c[3], c[4], c[5])
        elif c[1] == "switch":
            light.switch(c[2], c[3], c[4], c[5])

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