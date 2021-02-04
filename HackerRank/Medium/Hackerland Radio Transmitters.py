#!/bin/python3
# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
# DP, Search(?), Array

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    Hackerland = []
    for i in x:
        while int(i)>=len(Hackerland):
            Hackerland.append(False)
        Hackerland[int(i)]=True
    
    coverage = -1
    sindex = -1
    lindex = -1
    
    result = 0
    for i in range(len(Hackerland)):
        if i <= coverage:
           Hackerland[i] = False
        else: 
            if Hackerland[i]==True and sindex < 0:
                sindex = i
            elif Hackerland[i]==True and sindex >= 0:
                if i-sindex > k:
                    coverage = lindex + k
                    result += 1
                    if coverage < i:
                        sindex = i
                    else:
                        sindex = -1
                elif i-sindex == k:
                    result += 1
                    coverage = i+k
                    sindex = -1
                else:
                    lindex = i
    
    if sindex >= 0:
        result += 1    
    return result
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
