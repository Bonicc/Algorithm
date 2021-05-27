def dfs(src, tickets, visited, answer):
    for i, t in enumerate(tickets):
        if t[0] == src and visited[i] == 0:
            dest = t[1]            
            answer.append(dest)
            visited[i] = 1
                        
            dfs(dest, tickets, visited, answer)
            if 0 not in visited:
                return answer
            else:
                answer.pop()
                visited[i] = 0
                
    return answer

def solution(tickets):
    answer = ["ICN"]
    tickets.sort()
    visited = [0 for i in range(len(tickets))]
    src = "ICN"
    return dfs(src,tickets,visited,answer)
