def solution(n):
    answer = [1,2]
    for i in range(2,n):
        answer.append((answer[i-1]+answer[i-2])%1000000007)
    return answer[n-1]