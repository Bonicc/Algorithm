#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    
    map<string, int> m;
    for(auto i = clothes.begin(); i != clothes.end(); ++i){
        if(m[(*i)[1]])
            m[(*i)[1]] += 1;
        else
            m[(*i)[1]] = 1;;
    }
    
    for(auto i = m.begin(); i != m.end(); ++i)
        answer *= i->second + 1;
    
    return answer -1;
}