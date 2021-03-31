#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int> heap;
    for(int i=0 ;i<scoville.size();++i)
        heap.push(-scoville[i]);
    
    int top1, top2;
    while(-heap.top() < K ){
        top1 = heap.top();
        heap.pop();
        if(heap.size()==0)
            return -1;
        top2 = heap.top();
        heap.pop();
        heap.push(top1+top2*2);
        answer++;
    }
    
    return answer;
}