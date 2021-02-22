def solution(brown, yellow):
    answer = []
    for i in range(3, 2000):
        for j in range(i, 2000):
            if i * j == sum([brown,yellow]) and (i-2) * (j-2) == yellow:
                return [j, i]
    return answer