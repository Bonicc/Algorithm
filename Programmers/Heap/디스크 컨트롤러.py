import heapq as hq

def solution(jobs):
    answer = 0
    heap = []
    jobs.sort()
    end_time = 0
    i = 0
    
    while i<len(jobs):
        if end_time>jobs[i][0]:
            hq.heappush(heap,[jobs[i][1],jobs[i][0]])
            i+=1
        else: #end_time <= jobs[i][0]
            if heap == []:
                end_time = jobs[i][0]+jobs[i][1]
                answer += jobs[i][1]
                i+=1
            else:
                mean_time_jobs = hq.heappop(heap)
                end_time += mean_time_jobs[0]
                answer += end_time - mean_time_jobs[1]
                    
    while heap != []:
        mean_time_jobs = hq.heappop(heap)
        end_time += mean_time_jobs[0]
        answer += end_time - mean_time_jobs[1]
    
    return answer//len(jobs)