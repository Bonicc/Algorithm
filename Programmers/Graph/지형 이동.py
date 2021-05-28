def make_graph(land):
    graph = {}
    rl = len(land)
    cl = len(land[0])
    for i in range(rl):
        for j in range(cl):             
            index = i * cl + j
            
            if i - 1 >= 0:
                nindex = (i-1) * cl + j
                edge = abs(land[i-1][j] - land[i][j])                
                graph[tuple(sorted([index,nindex]))] = edge
            if j - 1 >= 0:
                nindex = i * cl + j-1
                edge = abs(land[i][j-1] - land[i][j])                
                graph[tuple(sorted([index,nindex]))] = edge
            if i + 1 < rl:
                nindex = (i+1) * cl + j
                edge = abs(land[i+1][j] - land[i][j])                
                graph[tuple(sorted([index,nindex]))] = edge
            if j + 1 < cl:
                nindex = i * cl + j+1
                edge = abs(land[i][j+1] - land[i][j])                
                graph[tuple(sorted([index,nindex]))] = edge
                
    return graph

def solution(land, height):
    answer = 0
    graph = make_graph(land)
    
    sorted_by_edge = sorted([[i, v] for v,i in graph.items()])
    
    mst_set = []
    set_index = 0
    mst_set_number = {}    
    
    for i, n in sorted_by_edge:
        if n[0] not in mst_set_number and n[1] not in mst_set_number:
            answer += i * (i > height)
            
            new_set = set()
            new_set.add(n[0])
            new_set.add(n[1])
            
            mst_set.append(new_set)
            
            mst_set_number[n[0]] = set_index
            mst_set_number[n[1]] = set_index
            
            set_index += 1
            
        elif n[0] not in mst_set_number and n[1] in mst_set_number:
            answer += i * (i > height)
            
            set_i = mst_set_number[n[1]]
            mst_set[set_i].add(n[0])
            
            mst_set_number[n[0]] = set_i
        
        elif n[0] in mst_set_number and n[1] not in mst_set_number:
            answer += i * (i > height)
            
            set_i = mst_set_number[n[0]]
            mst_set[set_i].add(n[1])
            
            mst_set_number[n[1]] = set_i
        
        if n[0] in mst_set_number and n[1] in mst_set_number:
            
            set_1 = mst_set_number[n[0]]
            set_2 = mst_set_number[n[1]]
            
            if set_1 == set_2:
                continue
            
            answer += i * (i > height)
            
            min_set_num = min(set_1,set_2)
            max_set_num = max(set_1,set_2)
            
            for element in mst_set[max_set_num]:
                mst_set_number[element] = min_set_num
            
            mst_set[min_set_num] = mst_set[min_set_num].union(mst_set[max_set_num])
            
        if len(mst_set[0]) == len(land)**2:
            break
                
    return answer