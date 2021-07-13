#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;


bool compare_song_plays(pair<int, int> a, pair<int, int> b){
    // 노래 별로 plays로 정렬하고, plays 가 같을경우 index로 정렬
    if(a.second == b.second)
        return a.first <= b.first;
    else
        return a.second >= b.second;
}

bool compare_genre_plays(pair<string, int> a, pair<string, int> b){
    // 장르별로 플레이 된 횟수를 기준으로 내림차순 정렬
    return a.second >= b.second; 
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    
    // genre의 전체 play 횟수를 저장하는 hash : genre_m 
    // genre의 각각 play 횟수 및 index 를 저장하는 song_m
    map<string, vector<pair<int, int>>> song_m;
    map<string, int> genre_m;
    
    for(int i = 0; i<genres.size(); i++){
        song_m[genres[i]].insert(song_m[genres[i]].end(), pair<int, int>(i, plays[i]));
        genre_m[genres[i]] += plays[i];
    }
    
    // 장르 플레이 수를 기준으로 정렬
    // 장르 해시를 벡터로 전환하고, sort를 활용하여 정렬한다.
    vector<pair<string, int>> vec(genre_m.begin(), genre_m.end());
    sort(vec.begin(), vec.end(), compare_genre_plays);
        
    // 전체 plays 순서대로 정렬된 벡터의 genre 순서 별로
    for(auto i = vec.begin(); i!= vec.end(); ++i){
        string gen = (*i).first;  // genre의 이름        
        vector<pair<int, int>> svec = song_m[gen]; 
        
        // 각 노래별로 plays 와 index 기준으로 정렬
        sort(svec.begin(), svec.end(), compare_song_plays);        
    
        int count = 0; // 최대 2곡 수록하기 위한 count
        for(auto j = svec.begin(); j!= svec.end();++j){
            if(count == 2)
                break;
            answer.insert(answer.end(), (*j).first);
            ++count;
        }
    }
            
    return answer;
}