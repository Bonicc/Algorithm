def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[0])
    prev_out = routes[0][1]
    for i in range(1,len(routes)):
        if prev_out < routes[i][0]:
            answer += 1
            prev_out = routes[i][1]
            continue
        prev_out = min(prev_out,routes[i][1])
    return answer+1