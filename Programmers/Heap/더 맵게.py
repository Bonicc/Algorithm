import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    
    while True:
        b1 = hq.heappop(scoville)
        if b1 > K:
            return answer
        else:
            try:
                b2 = hq.heappop(scoville)
                hq.heappush(scoville,b1+b2*2)
                answer += 1
            except:
                return -1    
    return answer