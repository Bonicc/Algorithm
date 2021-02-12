def solution(clothes):
    answer = 1
    hash_ = dict()
    for i in range(len(clothes)):
        try:
            hash_[clothes[i][1]] += 1
        except:
            hash_[clothes[i][1]] = 1
    for i in list(map(lambda x:x+1, hash_.values())):
        answer *= i
    return answer - 1