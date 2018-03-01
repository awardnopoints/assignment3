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
import urllib.error

def main():
    
    script_dir = os.path.dirname(__file__)
    tempinput = os.path.join(script_dir, "tempinput.txt")

    
    if len(sys.argv) < 2:
        target = input("Please input the filename or URL you would like to pass into the program.")
    else:
        target = sys.argv[1]
    
    if target[0:7] == 'http://':
        
        try:
            conn = urllib.request.urlopen(target)
        except urllib.error.HTTPError as e:
            print('HTTPError: {}'.format(e.code))
            print("Webpage not found.")
            sys.exit(1)
        except urllib.error.URLERror as e:
            print('URLError: {}'.format(e.reason))
            sys.exit(1)
        else:
            print("Valid URL")
        
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
        print("Executing command", i, "/", len(lines)-1)
        obey(lines[i], myLight)
    print(myLight.count(), "lights on.")
    if os.path.isfile(tempinput):
        os.remove(tempinput)
        
def obey(command, light):
    c = regexInterpret(command)
    if c[0]:
        for j in range(2,6):
            c[j] = int(c[j])
            if c[j] < 0:
                c[j] = 0
            elif c[j] >= light.side:
                c[j] = light.side-1
        print(c)
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
    
    
if __name__ == '__main__':
    main()