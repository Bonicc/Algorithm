#!/bin/python3
# https://www.hackerrank.com/challenges/torque-and-development/problem
# DFS, graph

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road >= c_lib:
        return n * c_lib
    
    cost = 0
    
    sorted_cities = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    
    for i,j in cities:
        sorted_cities[i-1].append(j-1)
        sorted_cities[j-1].append(i-1)
    
    stack = []
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            cost += c_lib
            stack.append(i)
        
        while len(stack) != 0:
            next_ = stack.pop()
            for j in sorted_cities[next_]:
                if visited[j] == 0:
                    visited[j] = 1
                    cost += c_road
                    stack.append(j)
                    
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
