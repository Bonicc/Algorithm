def solution(m, n, puddles):
    map_ = [[0 for i in range(m+1)] for i in range(n+1)]
    map_[1][1]=1
        
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] not in puddles:
                map_[i][j] += map_[i-1][j]+map_[i][j-1]
    return map_[n][m]%1000000007