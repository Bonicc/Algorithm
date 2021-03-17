def solution(arrows):
    answer = 0
    move = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1),(0,-1),(-1,-1)]
    point_direction = dict()
    position = (0,0)    
    point_direction[position] = [0,0,0,0,0,0,0,0]    
    for i in arrows:
        point_direction[position][i] = 1
        
        # 대각선 이동 시에 점이 아닌 선분과 만날 경우도 생각
        if i in [1,3,5,7]:
            check_cross_position = tuple(map(lambda x,y:x+y,position,move[(i+1)%8]))
        position = tuple(map(lambda x,y:x+y,position,move[i]))
        try:
            # 이미 해당 점을 거쳤을 경우
            # 만약 이미 그려진 선분으로 온 길이 아니라면
            # 도형을 하나 만들게 됨
            if point_direction[position][i-4] != 1:
                answer +=1
                point_direction[position][i-4] = 1
                
                if i in [1,3,5,7]:
                    try:
                        if point_direction[check_cross_position][i-2] == 1:
                            answer +=1
                    except:
                        pass
        except:
            # 만약 점을 거치지 않은 경우
            # 절대로 도형을 만들지 않음
            # 왔던 방향으로 선분을 그려줌
            point_direction[position] = [0,0,0,0,0,0,0,0]
            point_direction[position][i-4] = 1
            if i in [1,3,5,7]:
                try:
                    if point_direction[check_cross_position][i-2] == 1:
                        answer +=1
                except:
                    pass
    return answer