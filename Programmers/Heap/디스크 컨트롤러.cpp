#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

bool compare(vector<int> a, vector<int> b){
    return a[0] < b[0];
}

int solution(vector<vector<int>> jobs) {
    // heap을 사용하여 가장 시간이 짧은 작업부터 순서대로 처리
    // 요청부터 완료까지 저장해야하므로 (int, int)를 받는 pq를 저장
    // pq는 기본적으로 pair로 저장될 경우 first second 순서로
    // 큰 순서대로 저장하므로, 저장 시에 -1 을 곱해줘 가장 짧은 작업가
    // 가장 큰값이 될 수 있도록 저장한다.
    int answer = 0;
    
    // int의 쌍으로 되어있는 pq 선언
    // 단위 시간에 따른 계산을 위해 요청한 작업 순서대로 정렬해준다.
    // job의 순서가 요청 순서가 아닐 수 있으므로 먼저 sorting 해준다.
    priority_queue<pair<int,int>> pq; 
    sort(jobs.begin(), jobs.end(), compare);
    
    
    int j = 0;
    int end_time = 0;
    

    // 시간이 흘러가는 시뮬레이션을 진행하며,
    // 현재 진행중인 작업가 존재하지 않을 경우에는 현재 시간을 기준으로
    // 가장 빨리 끝낼 수 있는 작업가 끝나는 시간을 계산한다.
    // 진행 중인 작업가 존재할 경우에는 다음 시간으로 넘어간다.
    for(int i = 0; i < jobs[jobs.size() - 1][0] + 1; ++i){
        
        // 현재 시간에서 요청된 작업를 모두 pq안에 넣는다.
        while(j < jobs.size()){            
            if(jobs[j][0] != i)
                break;
            pq.push(pair<int, int>(-jobs[j][1], jobs[j][0]));
            ++j;
        }
        
        // 현재 작업를 하는 경우나 요청된 작업가 없을 경우에는 다음 시간으로 넘어간다.
        if(pq.empty() || end_time > i)
            continue;
        
        // 작업가 존재하고, 진행중인 작업가 없을 경우에는 다음 작업가 끝나는 시간을 계산한다.
        pair<int, int> next_job = pq.top();
        pq.pop();
        end_time = i + (-next_job.first); // 꺼낼 때는 -1을 한번 더 곱해준다.
        answer += end_time-next_job.second;
    }        
        
    
    // pq가 빌 때 까지 요청되었던 모든 작업를 작업의 진행 시간이 짧은 순서대로 처리한다.
    while(!pq.empty()){
        pair<int, int> next_job = pq.top();
        pq.pop();
        end_time += (-next_job.first);
        answer += end_time - next_job.second;        
    }
        
    return answer/jobs.size();
}