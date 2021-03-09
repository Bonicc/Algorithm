def solution(n, computers):
    answer = 0
    connected = [[] for _ in range(len(computers))]
    visited = [0 for _ in range(len(computers))]
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j] == 1:
                connected[i].append(j)
                
    s = []
    while True:
        if 0 in visited:
            answer +=1
            for i in range(n):
                if visited[i] == 0:
                    s.append(i)
                    visited[i] = 1
                    break
                    
            while s != []:
                p = s.pop()
                for i in connected[p]:
                    if visited[i] ==0:
                        s.append(i)
                        visited[i] = 1
        else:
            break
    
    return answer