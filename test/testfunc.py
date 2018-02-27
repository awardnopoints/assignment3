#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:17:34 2018

@author: eoin
"""
import ledCheck.light as l

def test_grids(n):
        myTest = l.Light(n)
        count = 0
        for i in myTest.grid:
            for j in i:
                count += 1
        return count