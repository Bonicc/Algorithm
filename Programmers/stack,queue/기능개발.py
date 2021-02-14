def solution(progresses, speeds):
    answer = []
    need_day = list(map(lambda x,y: (int((100-x)/y)) + 1 * (int((100-x)/y) != (100-x)/y) ,progresses,speeds))
    max = [need_day[0],0]
    for i in range(len(need_day)):
        if need_day[i] > max[0]:
            answer.append(i-max[1])
            max = [need_day[i],i]
    answer.append(len(need_day)-max[1])
    return answer