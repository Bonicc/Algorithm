def solution(prices):
    answer = [0 for _ in range(len(prices))]
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j] or j == len(prices)-1:
                answer[i] = j-i
                break
    return answer