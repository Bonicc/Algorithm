#!/bin/python3
# https://www.hackerrank.com/challenges/fibonacci-modified/problem
# DP, Array

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    tn = [t1,t2]
    for i in range(n-1):
        tn.append(tn[i]+tn[i+1]**2)        
    return tn[n-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
