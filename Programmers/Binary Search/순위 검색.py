def solution(info, query):
    answer = []
    lang = ["cpp","java","python","-"]
    job = ["backend","frontend","-"]
    years = ["junior","senior","-"]
    soulfood = ["chicken","pizza","-"]
    
    db = {}
    for i in info:
        a,b,c,d,e = i.split()        
        for l in [a[0],"-"]:
            for j in [b[0],"-"]:
                for y in [c[0],"-"]:
                    for s in [d[0],"-"]:
                        try:
                            db[l+j+y+s].append(int(e))
                        except:
                            db[l+j+y+s] = [int(e)]
    for i in db:
        db[i].sort()    
        
    for q in query:
        a,b,c,de = q.split(" and ")
        d,e = de.split(" ")
        dbi = a[0]+b[0]+c[0]+d[0]
        score = int(e)
        
        try:
            if db[dbi][-1] < score:
                answer.append(0)
                continue
            ## 이분탐색
            
            l = db[dbi]
            start = 0
            end = len(l)-1
            
            while start < end:
                mid = int((start+end)/2)                
                if score > l[mid]:
                    start = mid+1
                else:
                    end = mid                
            answer.append(len(l)-end)
            
            ## 이분탐색 끝
        except:
            answer.append(0)        
        
    return answer