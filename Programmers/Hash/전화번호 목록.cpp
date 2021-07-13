#include <string>
#include <vector>
#include <algorithm>

using namespace std;


bool solution(vector<string> phone_book) {
    sort(phone_book.begin(), phone_book.end());
        
    for(auto i = phone_book.begin(); i!= phone_book.end()-1; ++i)
    {
        if( (*i) == (*(i+1)).substr(0, (*i).length()))
            return false;
    }
    return true;
}