def solution(n, results):
    answer = 0
    graph1 = [[999 for i in range(n)] for j in range(n)]
    graph2 = [[999 for i in range(n)] for j in range(n)]
    for i in range(n):
        graph1[i][i] = 0
        graph2[i][i] = 0
    
    for [i,j] in results:
        graph1[i-1][j-1] = 1
        graph2[j-1][i-1] = 1
            
    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph1[i][j] = min(graph1[i][j],graph1[i][k]+graph1[k][j])
                graph2[i][j] = min(graph2[i][j],graph2[i][k]+graph2[k][j])
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph1[i][j] = min(graph1[i][j],graph1[i][k]+graph1[k][j])
                graph2[i][j] = min(graph2[i][j],graph2[i][k]+graph2[k][j])
                
    for i in range(n):
        result = [0 for _ in range(n)]
        for j in range(n):
            if graph1[i][j] != 999 or graph2[i][j]!= 999:
                result[j] = 1
        if 0 not in result:
            answer+=1
    
    return answer