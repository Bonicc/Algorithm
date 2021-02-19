import heapq as hq

def solution(operations):
    answer = [0,0]
    maxh = []
    minh = []
    heap_len = 0
    for i in operations:
        O, V = i.split()
        if O == 'I':
            heap_len +=1
            hq.heappush(maxh,-int(V))
            hq.heappush(minh,int(V))
        elif O == "D":
            if int(V) < 0 and heap_len !=0:
                hq.heappop(minh)
            elif int(V) >0 and heap_len != 0:
                hq.heappop(maxh)
            heap_len = max(heap_len-1,0)
        if heap_len == 0:
            maxh, minh = [], []
    if heap_len != 0:
        answer = [-maxh[0], minh[0]]
    return answer
