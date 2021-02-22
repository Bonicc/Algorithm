from collections import deque

def solution(priorities, location):
    answer = 0
    pri = deque(enumerate(priorities))
    value = pri.popleft()
    while True:
        Printed = True
        for i in range(len(pri)):
            if pri[i][1] > value[1]:
                pri.append(value)
                Printed = False
                break
        if Printed is True:
            answer +=1
            if value[0]==location:
                break
        value = pri.popleft()
    return answer