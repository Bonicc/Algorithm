#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    s = list(map(lambda x:x%k,s))
    snumber = [s.count(i) for i in range(k)]
    
    print(snumber)
    
    answer = 0    
    for i in range(1,len(snumber)):
        if i >= k/2:
            break
        answer += max(snumber[i],snumber[k-i])
        
    if snumber[0]>= 1:
        answer +=1
    if k%2 ==0 and snumber[k//2]>=1:
        answer +=1
        
    return answer
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
