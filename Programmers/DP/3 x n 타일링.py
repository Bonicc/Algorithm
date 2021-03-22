def solution(n):
    answer = [0,0,3,0,11]
    for i in range(5,n+1):
        if i % 2 == 1:
            answer.append(0)
        else:
            answer.append((answer[i-2]*4-answer[i-4])%1000000007)
    return answer[n]