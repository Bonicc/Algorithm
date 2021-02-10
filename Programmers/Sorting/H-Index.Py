def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    h_index = citations[0]
    h_index_count = 0
    for i in range(len(citations)):
        if h_index_count < citations[i]:
            h_index_count+=1
        else:
            break
            
    answer = h_index_count            
    return answer