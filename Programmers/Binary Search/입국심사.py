def solution(n, times):
    end = max(times) * n
    start = min(times)
    answer = min(times)
    while start<=end:
        mid = int((start+end)/2)
        if sum(list(map(lambda x: mid//x,times))) >= n:
            answer = mid
            end = mid-1
        else:
            start = mid+1            
    return answer