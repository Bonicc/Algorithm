from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    word_length = len(words[0])
    words.append(begin)
    connected = dict()
    visited = dict()
    
    for i in range(len(words)):
        connected[words[i]] = []
        visited[words[i]] = 0
        for j in range(len(words)):
            if i!=j and sum(map(lambda x,y: x==y, list(words[i]),list(words[j]))) == word_length-1:
                connected[words[i]].append(words[j])
    
    q.append(begin)
    visited[begin] = 1
    done = 0
    while 0 in visited.values() and done == 0:
        answer += 1
        t = len(q)
        while t != 0:
            temp = q.popleft()
            if temp == target and done ==1:
                done = 1
                break
                
            for i in connected[temp]:
                if visited[i] ==0:
                    if i != target:
                        visited[i] = 1
                        q.append(i)
                    if i == target:
                        done = 1
                        break
                
            t -= 1
        
    return done * answer