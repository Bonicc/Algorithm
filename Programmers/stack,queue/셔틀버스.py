from collections import deque 

def solution(n, t, m, timetable):
    answer = ''
    # for 9:00 ~ 18:00
    time_limit = [ 9*60 +  i * t for i in range(n)] + [0,1440]
    time_queue = [deque() for i in range(n+1)]
    timetable_int = list(map(lambda x: int(x.split(":")[0])*60+int(x.split(":")[1]), timetable))
    
    time_limit.sort()
    timetable_int.sort()
    
    for tt in timetable_int:
        for bt in range(n+1):
            if time_limit[bt] < tt and tt <= time_limit[bt+1]:
                for lt in range(bt,n+1):
                    if len(time_queue[lt]) < m:
                        time_queue[lt].append(tt)
                        break
        
    time_queue = time_queue[:-1]        
    late_time = 0
    for dq in range(len(time_queue)):
        if len(time_queue[dq])<m:
            late_time = time_limit[dq+1]
        elif len(time_queue[dq])>=m:
            late_time = time_queue[dq][m-1]-1
    
    late_time_str = [str(int(late_time/60)),":",str(int(late_time%60))]
    while len(late_time_str[0])<=1:
        late_time_str[0]="0"+late_time_str[0]
    while len(late_time_str[2])<=1:
        late_time_str[2]="0"+late_time_str[2]
    
    return "".join(late_time_str)