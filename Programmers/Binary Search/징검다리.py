def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    
    start, end = 1,distance    
    while start < end:
        prev_rock = 0
        destroyed_rock_count = 0
        mid = int((start+end)/2)
        
        for r in rocks:
            if r - prev_rock <= mid:
                destroyed_rock_count += 1
            else:
                prev_rock = r
                
        if distance - prev_rock < mid:
            destroyed_rock_count += 1
        
        if destroyed_rock_count <= n:
            start = mid + 1
        else:
            end = mid
        
    return end