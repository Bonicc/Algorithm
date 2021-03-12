from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    for i,j in edge:
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)
        
    q = deque()
    q.append(0)
    visited[0] = 1
    while True:
        t = len(q)
        answer = len(q)
        while t!=0:
            node = q.popleft()
            for i in range(len(graph[node])):
                if visited[graph[node][i]]==0:
                    q.append(graph[node][i])
                    visited[graph[node][i]]=1
            t-=1
        if len(q) == 0:
            return answer