#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    sort(participant.begin(), participant.end());
    sort(completion.begin(),completion.end());        
    int n = completion.size();
    for(int i =0; i<n; i++)
        if(participant[i]!=completion[i])
            return participant[i];
    return participant[n];
}