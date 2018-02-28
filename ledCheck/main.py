#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 09:36:01 2018

@author: eoin
"""

import ledCheck.light as l
import sys
import re
import os
import urllib.request

def main():
    if len(sys.argv) < 2:
        target = input("Please input the filename or URL you would like to pass into the program.")
    else:
        target = sys.argv[1]
    if target[0:7] == 'http://':
        script_dir = os.path.dirname(__file__)
        tempinput = os.path.join(script_dir, "tempinput.txt")
        with urllib.request.urlopen(target) as response, open(tempinput, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
            myfile = open(tempinput, 'r')
    else:
        myfile = open(target, 'r')
    lines = list(myfile)
    L = int(lines[0])
    myLight = l.Light(L)
    print("There are", len(lines)-1, "commands to execute.")
    for i in range(1, len(lines)):
#        if i == 1 or i % 50 == 0 or i == len(lines)-1:
        print("Executing command", i, "/", len(lines)-1)
        obey(lines[i], myLight)
    print(myLight.count(), "lights on.")
    if os.path.isfile(tempinput):
        os.remove(tempinput)
        
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