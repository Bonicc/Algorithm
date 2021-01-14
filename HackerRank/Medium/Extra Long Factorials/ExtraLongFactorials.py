# ExtraLongFactorials

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    result = []
    result.append(1)    
    
    length_of_each_number = 9
    
    divider = int(10**length_of_each_number)    
    for i in range(n):
        for j in range(len(result)):
            result[j] = result[j] * (i+1)
                        
        for j in range(len(result)):
            if result[j]//divider >=1:
                if j == len(result)-1:
                    result.append(result[j]//divider)
                else:
                    result[j+1] = result[j+1]+result[j]//divider
            result[j] = result[j] % divider
                    
    result = [str(int) for int in result]
    for i in range(len(result)):
        if len(result)-1!=i:
            for j in range(length_of_each_number - len(result[i])):
                result[i] = "0" + result[i]
    return result

if __name__ == '__main__':
    n = int(input())

    result_array = extraLongFactorials(n)
    result = ""
    for i in range(len(result_array)):
        result = result+result_array[len(result_array)-i-1]
    print(result)