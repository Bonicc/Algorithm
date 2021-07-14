#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    // stack을 이용하여, 가격이 떨어지면 pop 하고 아니면 냅둔다.
    // 인자를 시간으로 넣어 가격이 떨어지지 않은 시간을 계산한다.
    
    vector<int> answer;
    int temp = prices.size();
    // 계산 편의성을 위한 answer의 size만큼 만큼 0을 넣는다
    while(temp-- > 0)
        answer.push_back(0);
    
    // stack은 vector로 선언하여 계산
    vector<pair<int, int>> stack;
    for(int i = 0; i<prices.size(); ++i){
        // 스택이 비어있을 경우 에러를 막기위해 무조건 넣는다.
        if(stack.empty())
            stack.push_back(pair<int, int>(prices[i], i));
        else{
            // stack 이 비기 전까지 가격 비교를 통해 떨어졌는지 확인하고
            // 떨어지면 해당 가격이 들어온 시간을 비교해 현재 시간과의 차이를 구한다.
            // 안떨어지면 다음 prices로 넘어간다.
            while(!stack.empty()){
                if(stack.back().first > prices[i]){
                    int time = stack.back().second;
                    stack.pop_back();
                    answer[time] = i-time;
                }
                else
                    break;
            }
            stack.push_back(pair<int, int>(prices[i], i));    
        }
    }    
    while(!stack.empty()){
        // stack을 모두 비우기 위한 후처리를 진행한다.
        // 마지막까지 가격이 떨어지지 않은 주식들이므로, 
        // 마지막 시간과 들어간 시간의 차를 넣어준다.
        int time = stack.back().second;
        stack.pop_back();
        // index 와의 계산이므로 size-1 과의 시간을 계산한다.
        answer[time] = (prices.size() - 1) - time ; 
    }
    return answer;
}