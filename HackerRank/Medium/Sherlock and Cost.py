#!/bin/python3
# https://www.hackerrank.com/challenges/sherlock-and-cost/problem
# DP, Array

import math
import os
import random
import re
import sys

# Complete the cost function below.
def cost(B):
    arr = []
    for i in range(len(B)):
        if i ==0:
            arr.append([0,0])
        else:
            max1 = max( arr[i-1][0] + abs(1-1), arr[i-1][1] + abs(B[i-1]-1))
            max2 = max( arr[i-1][0] + abs(1-B[i]), arr[i-1][1] + abs(B[i-1]-B[i]))
            arr.append([max1, max2])
           
    return max(arr.pop())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
