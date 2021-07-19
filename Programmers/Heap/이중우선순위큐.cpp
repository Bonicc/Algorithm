#include <string>
#include <vector>
#include <queue>

using namespace std;
vector<int> solution(vector<string> operations) {
    vector<int> answer;
    
    // priority queue는 가장 큰 값이 가장 우선순위
    // 가장 큰 값을 순서대로 저장하는 pq1
    // 가장 작은 값을 순서대로 저장하는 pq2
    // 두 pq를 공유하는 size를 나타내는 pq_size
    priority_queue<int> pq1, pq2;    
    int pq_size = 0;
    
    for(auto &i:operations){
        char command = i[0];
        int number = stoi(i.substr(2,size(i)-2));
                
        // 명령어가 I 이면, pq_size를 하나 늘리고, 
        // 각 pq1에는 number, pq2에는 최소값이 우선순위인 -number를 넣어준다.
        if(command == 'I'){
            ++pq_size;
            pq1.push(number);
            pq2.push(-number);
        }            
        else{
            // pq_size가 0 이하이면 0으로 수렴하도록
            pq_size = --pq_size > 0 ? pq_size : 0;
            
            // size 가 0일경우엔 pq1, pq2를 모두 비워준다.
            if(pq_size == 0){
                while(!pq1.empty())
                    pq1.pop();
                while(!pq2.empty())
                    pq2.pop();
            }
            // size 가 0이 아니면, 해당되는 pq에서 하나씩 뺀다.       
            else{
                if(number == 1)
                    pq1.pop();
                else{
                    pq2.pop();
                }
            }
        }
    }
        
    // pq_size에 따라 answer에 값을 넣어준다.
    if(pq_size != 0){
        answer.push_back(pq1.top());
        answer.push_back(-pq2.top());
    }
    else{
        answer.push_back(0);
        answer.push_back(0);
    }
    
    return answer;
}