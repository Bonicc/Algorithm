#!/bin/python3
# https://www.hackerrank.com/challenges/the-power-sum/problem
# Recursive

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
def powerSum(X, N, V):
    value = V**N
    if X-value<0:
        return 0
    elif X-value==0:
        return 1
    else:
        return powerSum(X-V**N,N,V+1) + powerSum(X,N,V+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N, 1)

    fptr.write(str(result) + '\n')

    fptr.close()
