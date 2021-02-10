# ClimingtheLeaderboard
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
# Sort, Insertion Sort

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked_rank = []
    temp_num = ranked[0]
    rank = 1
    for i in ranked:
        rank = rank + int(temp_num!=i)
        temp_num = i
        ranked_rank.append(rank)
        
    result = []
    temp_j = len(ranked)-1
    for i in player:      
        while(temp_j >=0):
            if i<ranked[temp_j]:
                result.append(ranked_rank[temp_j]+1)
                break
            elif i==ranked[temp_j]:
                result.append(ranked_rank[temp_j])            
                break
            temp_j = temp_j-1
        if temp_j <0:
            result.append(1);
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
