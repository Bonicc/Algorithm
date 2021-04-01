#include <string>
#include <vector>
#include <set>
#include <iterator>

using namespace std;

int solution(int N, int number) {
    int answer = 0;
    vector<set<int>> number_set(9);
    
    int op = 0;
    for(int i=1 ; i<9; ++i){
        op = op*10+1;
        number_set[i].insert(op*N);
    }
    
    for(int i = 1 ; i < 9; ++i){
        for(int j = 1; j<i; ++j ){
            int k = i - j;
            set<int>::iterator iter1;
            set<int>::iterator iter2;
            for(iter1 = number_set[j].begin(); iter1 != number_set[j].end(); iter1++)
                for(iter2 = number_set[k].begin(); iter2 != number_set[k].end(); iter2++){
                    int temp_number1 = *iter1;
                    int temp_number2 = *iter2;
                    if (temp_number1+temp_number2<=32001)
                        number_set[i].insert(temp_number1+temp_number2);
                    if (temp_number1*temp_number2<=32001)
                        number_set[i].insert(temp_number1*temp_number2);
                    if (temp_number1-temp_number2>=0)
                        number_set[i].insert(temp_number1-temp_number2);
                    if(temp_number2!=0)
                        number_set[i].insert(temp_number1 / temp_number2);
                }
            }
    if(number_set[i].find(number) != number_set[i].end())
        return i;          
    }
    if(answer == 0)
        return -1;
    
    return 0;
}