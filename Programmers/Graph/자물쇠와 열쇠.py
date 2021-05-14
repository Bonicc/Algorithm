import copy

def unlock(lock_expanded, key, r, c, M, N):
    for i in range(M):
        for j in range(M):
            lock_expanded[r+i][c+j] = (lock_expanded[r+i][c+j] ^ key[i][j])
    return is_unlock(lock_expanded, M, N)
        
def is_unlock(lock_expanded, M, N):
    unlocked = [[lock_expanded[M+j][M+i] for i in range(N)] for j in range(N)]
        
    if sum(map(sum,unlocked)) == N**2:
        return True
    return False

def solution(key, lock):
    
    M = len(key)
    N = len(lock)
    
    # make key set
    key2 = [[key[M-j-1][i] for j in range(M)] for i in range(M)]
    key3 = [[key[M-i-1][M-j-1] for j in range(M)] for i in range(M)]
    key4 = [[key[j][M-i-1] for j in range(M)] for i in range(M)]
        
    key_set = [key,key2,key3,key4]
    
    # make lock expanded to calculate the square of 1
    # when keys are added
    lock_expanded = [[0 for i in range(2*M+N+1)] for j in range(2*M+N+1)]
    for i in range(N):
        for j in range(N):
            lock_expanded[M+i][M+j] = lock[i][j]    
    
    # check each key can unlock the lock
    for key in key_set:        
        for i in range(M+N):
            for j in range(M+N):
                # check right-down
                cle = copy.deepcopy(lock_expanded)
                if unlock(cle, key, i, j, M, N):
                    return True
                                
    #without key
    if is_unlock(lock_expanded,M, N):
        return True
    
    return False