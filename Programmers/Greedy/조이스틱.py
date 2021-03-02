def solution(name):
    answer = 999999
    start_number = ord("A")
    end_number = start_number + 26
    rname = ''.join(reversed(name))
    rname = rname[-1]+rname[:-1]
    
    # 정방향
    for i in range(len(name)):
        temp = 0
        for j in range(len(name)):
            temp += min(ord(name[j])-start_number,end_number - ord(name[j]))
            for k in range(j+1, len(name)):
                if name[k] != "A":
                    temp += 1
                    break
        temp += min(len(name)-i,i)        
        name = name[1:] + name[0]     
        answer = min(answer+0, temp+0)
        
    # 역방향 
    for i in range(len(rname)):
        temp = 0
        for j in range(len(rname)):
            temp += min(ord(rname[j])-start_number,end_number - ord(rname[j]))
            for k in range(j+1, len(rname)):
                if rname[k] != "A":
                    temp += 1
                    break
        temp += min(len(rname)-i,i)        
        rname = rname[1:] + rname[0]     
        answer = min(answer+0, temp+0)
    return answer