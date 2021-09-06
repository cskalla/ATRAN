#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 13:04:32 2021

@author: carolineskalla
"""
import random
import numpy as np
import math
#Parameters:
#Number of functions
numfuncs = 9;
#Number of agents
numagents = 100;
#Number of tasks
numtasks = 10;
#Diversity jitter
agspread = 10;
#Agent total skill strength
anorm = 10;
gdivvals = np.logspace(-1, 3, 10)

for gdiv in gdivvals:
    
#gdiv = gdivvals[0] #testing
#exp((-(0:par.numfuncs-1).^2)/gdiv)
    x = (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))
    print("x:", x)
    print("x sum: ", sum(x))
    y=x/sum(x)
    print("y:",y)
    print("y sum: ", sum(y))
    
    #domf = np.random.choice(9, numagents, replace=True, p=x)
    #print(domf)