from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    complete = []
    bridge = deque([0 for _ in range(bridge_length)])
    bridge_weight = 0
    i = 0
    while True:
        answer += 1
        bridge_weight -= bridge.popleft()
        if bridge_weight + truck_weights[i] <= weight:
            bridge_weight += truck_weights[i]
            bridge.append(truck_weights[i])
            i+=1
        else:
            bridge.append(0)
        
        if i == len(truck_weights):
            while bridge_weight != 0:
                answer += 1
                bridge_weight -= bridge.popleft()
                
            break                
    return answer