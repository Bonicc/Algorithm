#!/bin/python3
# https://www.hackerrank.com/challenges/countingsort4/problem
# Sort

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    length = len(arr)
    
    result = []  
    for i in range(length):
        while(len(result)<int(arr[i][0])):
            result.append([])        
        
        if i < length/2:
            result[int(arr[i][0])].append("-")
        else:
            result[int(arr[i][0])].append(arr[i][1])
    
    result_arr = ""
    for i in range(len(result)):
        for j in result[i]:
            result_arr += j+ " "
            
    print(result_arr)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
