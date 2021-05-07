def solution(n, s, a, b, fares):
    g = [[100000001 * (i!=j) for i in range(n)] for j in range(n)]
    
    for f in fares:
        g[f[0]-1][f[1]-1] = f[2]
        g[f[1]-1][f[0]-1] = f[2]
                
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = min( g[i][k] + g[k][j] , g[i][j])
        
    return min([g[s-1][i] + g[i][a-1] + g[i][b-1] for i in range(n)])