#include <string>
#include <vector>
#include <deque>

using namespace std;

bool ismax(deque<pair<int,int>> q, pair<int, int> a){
    // deque 안에서 max 인지 확인하는 함수
    int compared_value = a.first;
    for(int i = 0; i<q.size(); ++i)
        if(compared_value < q[i].first)
            return 0;
    return 1;
}

int solution(vector<int> priorities, int location) {
    // value와 index로 이루어진 queue를 이용하여 
    // 우선 순위가 max인 것들을 뺴가면서 갯수를 센다.
    // 여기선 max 확인을 위해 인자를 확인할 수 있는 deque 사용
    int answer = 0;    
    deque<pair<int, int>> q;    
    
    // value 와 index 로 이루어진 값을 deque 안에 넣는다.
    for(int i = 0; i<priorities.size(); ++i)
        q.push_back(pair<int, int>(priorities[i], i));
    
    // deque가 빌 때 까지
    while(!q.empty()){
        // 가장 앞에 있는 것을 꺼내
        pair<int, int> temp = q.front();
        q.pop_front();
        
        // max 값인지 확인하고
        if(ismax(q, temp))
            // max면 index를 확인하고 맞으면 return 틀리면 순서 + 1
            if(temp.second == location)
                return answer + 1;
            else{
                ++answer;
                continue;
            }
        // max가 아니면, 그냥 다시 뒤에 넣는다.
        q.push_back(temp);
    }
    
    return answer;
}