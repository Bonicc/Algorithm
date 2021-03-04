def solution(money):
    money1, money2 = money[1:], money[:-1]
    money1[2], money2[2] = money1[0]+money1[2], money2[0]+money2[2]
    
    for i in range(3,len(money)-1):
        money1[i] += max(money1[i-2],money1[i-3])
        money2[i] += max(money2[i-2],money2[i-3])
            
    return max(money1[-1],money1[-2],money2[-1],money2[-2])