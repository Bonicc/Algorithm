#include <string>
#include <vector>

using namespace std;

int path[100][100];

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    path[0][0] = 1;
    for(int i =0; i<puddles.size(); i++)
        path[puddles[i][1]-1][puddles[i][0]-1] = -1;
            
    for(int i = 1; i<100; i++){
        if(path[0][i]!=-1)
            path[0][i] = (path[0][i-1]!=-1) ? path[0][i-1]:0;
        if(path[i][0]!=-1)
            path[i][0] = (path[i-1][0]!=-1) ? path[i-1][0]:0;
    }    
        
    for(int i = 1; i< n; i++)
        for(int j = 1; j< m; j++)
            if(path[i][j] != -1){
                if(path[i-1][j] != -1)
                    path[i][j] += path[i-1][j]%1000000007;
                if(path[i][j-1] != -1)
                    path[i][j] += path[i][j-1]%1000000007;
                path[i][j] %= 1000000007;
            }
    return path[n-1][m-1];
}
