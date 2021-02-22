from math import sqrt
from itertools import permutations

def isprime(n):
    if n <= 1:
        return 0
    else:
        for i in range(2, int(sqrt(n))+1):
            if n%i ==0:
                return 0
        return 1
            
def solution(numbers):
    combo = sum([list(map("".join,permutations(numbers, i+1))) for i in range(len(numbers))],[])
    answer = {}
    for i in range(len(combo)):
        try:answer[int(combo[i])]
        except:answer[int(combo[i])] = isprime(int(combo[i]))
    return sum(answer.values())