def solution(n, costs):
    answer = 0
    graph = [[] for _ in range(n)]
    for i in costs:
        graph[i[0]].append([i[1],i[2]])
        graph[i[1]].append([i[0],i[2]])
    
    connected = [0]    
    while len(connected) != n:
        min_ = 999999999
        for i in connected:
            for j in range(len(graph[i])):
                if graph[i][j][0] not in connected and min_ > graph[i][j][1]:
                    next_connect = graph[i][j][0]
                    min_ = graph[i][j][1]
                    
        connected.append(next_connect)
        answer += min_
        
    return answer