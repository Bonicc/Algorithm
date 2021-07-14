#include <string>
#include <vector>
#include <deque>

using namespace std;

int sum(deque<pair<int, int>> q){
    // 다리 위에 있는 트럭들의 무게 합
    if(q.empty())
        return 0;
    
    int answer = 0;
    for(auto& i: q)
        answer += i.first;
    return answer;
}


void after_one_time(deque<pair<int, int>> &q){
    // 다리 위에 있는 트럭들의 이동 거리를 한칸씩 이동 시켜줌
    if(q.empty())
        return;
    
    for(auto& i: q)
        i.second++;
    
    return;
}

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    // queue 를 활용하여 다리에 트럭을 놓고, 트럭의 무게 계산 및 시간계산을 통해
    // 최종적인 정답을 알아낸다.
    // 간단한 구현 문제
    
    int answer = 0;
    
    // 대기 트럭이 존재하는지 확인하기 위한 tw
    // 다리 위의 트럭의 무게와 이동 거리를 알아내는 truck_on_bridge 
    // 계산의 편이성을 위해 둘다 deque로 선언한다.
    deque<int> tw = deque(truck_weights.begin(), truck_weights.end());
    deque<pair<int, int>> truck_on_bridge;
    
    while(!tw.empty()){
        // answer는 시간
        // 1 단위의 시간이 지날 때 마다 다리 위의 트럭들이 1만큼 이동한다.
        ++answer;
        after_one_time(truck_on_bridge);
        
        // 트럭중에 다리 끝에 도달한게 있으면 빼준다.
        if(truck_on_bridge.front().second == bridge_length)
            truck_on_bridge.pop_front();
        
        // 다리 위의 트럭의 무게와 가장 앞에 대기한 트럭의 무게가 
        // 다리가 견딜 수 있는 무게 보다 높을 경우에는 계속 대기한다.
        if(sum(truck_on_bridge) + tw.front() > weight){
            continue;
        }
        
        // 견딜 수 있을 경우에는 대기 트럭 중 가장 앞의 트럭이 다리로 올라간다.
        int temp = tw.front();
        tw.pop_front();
        truck_on_bridge.push_back(pair<int, int>(temp, 0));
    }  
    
    // 대기 트럭이 존재하지 않을 경우, 다리 위 트럭이 전부 건너갈 때까지 시간을 잰다.
    while(!truck_on_bridge.empty()){
        ++answer;        
        after_one_time(truck_on_bridge);
        if(truck_on_bridge.front().second == bridge_length)
            truck_on_bridge.pop_front();        
    }
    return answer;
}