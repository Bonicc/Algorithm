def solution(answers):
    supoja = [[1,2,3,4,5] * -int(-10000/5), [2,1,2,3,2,4,2,5] * -int(-10000/7), [3,3,1,1,2,2,4,4,5,5] * -int(-10000/9)]
    count = [sum(list(map(lambda x,y : int(x==y), supoja[i][:len(answers)],answers))) for i in range(3)]
    return [i+1 for i in range(3) if list(map(lambda x: x==max(count),count))[i]==True]