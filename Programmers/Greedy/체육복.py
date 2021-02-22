def solution(n, lost, reserve):
    answer = 0
    newlost, newreserve = [i for i in lost if i not in reserve], [i for i in reserve if i not in lost]
    for i in range(len(newlost)):
        for j in range(len(newreserve)):
            if newlost[i] - 1 == newreserve[j] or newlost[i] + 1 == newreserve[j]:
                newreserve[j] = -2
                answer+=1
                break
    return n-len(newlost)+answer