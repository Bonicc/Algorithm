#!/bin/python3
# https://www.hackerrank.com/challenges/lilys-homework/problem
# Sorting

import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
def lilysHomework(arr):
    a = []
    for i, x in enumerate(arr):
        a.append([x,i])
    a_copy = a.copy()
    
    sa1 = sorted(a, key = lambda x : x[0])
    sa2 = sa1.copy()
    sa2.reverse()
    
    print(a_copy)
    print(sa1)
    
    result1 = 0    
    for i in range(len(a)):
        while a_copy[i][1] != sa1[i][1]:
            result1 += 1            
            j = sa1[i][1]
            sa1[i], sa1[j] = sa1[j], sa1[i]     
                
    result2 = 0
    for i in range(len(a)):
        while a_copy[i][1] != sa2[i][1]:
            result2 += 1
            j = sa2[i][1]
            sa2[i], sa2[j] = sa2[j], sa2[i]     
        
    return min(result1,result2)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
