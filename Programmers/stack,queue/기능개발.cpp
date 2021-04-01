#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> remain_time;
    for(int i =0; i < progresses.size(); ++i){
        remain_time.push_back(ceil((double(100)-double(progresses[i]))/double(speeds[i])));
    }
    
    int max = -1;
    int count = 0;
    for(int i =0; i<remain_time.size(); ++i){
        if(max == -1){
            max = remain_time[i];
            ++count;
        }
        else{
            if(max<remain_time[i]){
                answer.push_back(count);
                count = 1;
                max = remain_time[i];
            }
            else
                ++count;
        }
    }
    if(count !=0)
        answer.push_back(count);
    return answer;
}