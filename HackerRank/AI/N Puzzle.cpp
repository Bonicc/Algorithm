#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <queue>
#include <string>
using namespace std;

void print_puzzle(vector<vector<int>> puzzle){
    // see the puzzle's present status
    int puzzle_size = puzzle.size();
    
    for(int i = 0 ; i < puzzle_size; i++){
        for(int j = 0 ; j < puzzle_size; j++){
            printf("%d ",puzzle[i][j]);
        }
        printf("\n");
    }
}

pair<int, int> find_zeros_position(vector<vector<int>> puzzle){
    // find the position of zeros of puzzle
    
    pair<int, int> position;
    int puzzle_size = puzzle.size();
    for(int i = 0; i< puzzle_size; ++i){
        for(int j = 0; j<puzzle_size; ++j){
            if (puzzle[i][j] == 0){
                position.first = i;
                position.second = j;
            }
        }
    }
    
    return position;
}

vector<vector<int>> swap_position( vector<vector<int>> puzzle, int r, int c, int cr, int cc){
    // swap numbers in puzzle with given position
    vector<vector<int>> c_puzzle;
    c_puzzle.resize(puzzle.size());
    
    std::copy(puzzle.begin(), puzzle.end(), c_puzzle.begin());
    
    c_puzzle[r][c] = puzzle[cr][cc];
    c_puzzle[cr][cc] = puzzle[r][c];
        
    return c_puzzle;
}

int huristic_function(vector<vector<int>> puzzle){
    // calculate the score of the given puzzle's huristic function
    
    int puzzle_size = puzzle.size();
    int answer = 0;
    
    for(int i = 0; i < puzzle_size; ++i){
        for(int j = 0; j <puzzle_size; ++j){
            if(i*puzzle_size + j != puzzle[i][j]){
                ++answer;
            }
        }        
    }
    
    return answer;
}

struct Node{
    // Node in tree:
    // int parent_id    : parent's id
    // int move_count   : movement count from initial state
    // int huristic     : huristic functions value for given puzzle
    // pair<int, int> zero_position : the row and coulmn of zeros
    // vector<vector<int>> puzzle   : the puzzle
    // string direction_from_previos: movement direction from previous state
    
    int parent_id;
    int move_count;
    int huristic;
    pair<int, int> zero_position;
    vector<vector<int>> puzzle;
    string direction_from_previous;
};

struct compare{
    // to use comparison in pq for given pair of ints
    // the first of pair is huristic score that is sum of move_count and huristic functions result
    // the second one is an id of node
    
    // at this compare, we just get the minimum huristic score regardless of the id
    bool operator()(pair<int, int> a, pair<int, int> b){
        return a.first > b.first;
    }
};

int main(void) {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    vector<vector<int>> puzzle;
    
    int puzzle_size;
    cin >> puzzle_size;
    
    // get input as 2d - vector 
    for(int i = 0 ; i < puzzle_size; i++){
        vector<int> temp_vector;
        for(int j = 0 ; j < puzzle_size; j++){
            int number;
            cin >> number;
            temp_vector.push_back(number);
        }
        puzzle.push_back(temp_vector);
    }
    
    
    // make map based tree
    map<int, Node> tree_map;
    
    // make map to check the visited puzzle 
    map<vector<vector<int>>, bool> visited;    
    
    // The pair of priority queue is <huristic_score(int), node id(int)>
    priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq;
       
    
    int node_ids = 0;    
            
    // an initial node
    Node root;
        
    root.parent_id = node_ids;
    root.move_count = 0;
    root.huristic = huristic_function(puzzle);
    root.zero_position = find_zeros_position(puzzle);
    root.puzzle = puzzle;
    root.direction_from_previous = "None";
    
    visited[puzzle] = 1 ;    
    tree_map[node_ids] = root;
    pq.push(pair<int, int>(root.move_count + root.huristic, node_ids));
    
    
    // make vector of movement to calculate with for loop
    vector<pair<int, int>> next_move;
    next_move.push_back(pair<int, int>(-1, 0));
    next_move.push_back(pair<int, int>(1, 0));
    next_move.push_back(pair<int, int>(0, -1));
    next_move.push_back(pair<int, int>(0, 1));

    vector<string> next_move_str;
    next_move_str.push_back("UP");
    next_move_str.push_back("DOWN");
    next_move_str.push_back("LEFT");
    next_move_str.push_back("RIGHT");

    // priority queue's top
    pair<int, int> min_node_num;
    
    // node that temporarly get top of pq
    Node temp_node;

    while(1){
        min_node_num = pq.top();
        pq.pop();
        
        temp_node = tree_map[min_node_num.second];
        if(temp_node.huristic == 0)
            break;
        
        // present zero's position
        // present puzzle
        pair<int, int> present_position = temp_node.zero_position;
        vector<vector<int>> present_puzzle = temp_node.puzzle;
        
        // for any direction
        for(int i = 0; i< 4; ++i){
            pair<int, int> nm = next_move[i];
            string nms = next_move_str[i];
            
            // if I can move the puzzle in given direction
            if(present_position.first + nm.first >=0 && present_position.first + nm.first < puzzle_size &&
              present_position.second + nm.second >=0 && present_position.second + nm.second < puzzle_size){
                
                int nr = present_position.first + nm.first;
                int nc = present_position.second + nm.second;
                                
                vector<vector<int>> new_puzzle = swap_position(present_puzzle, 
                                                               present_position.first, present_position.second,
                                                              nr, nc);
                
                // and if I did not visite moved puzzle
                if(!visited[new_puzzle]){
                    Node new_node;

                    new_node.parent_id = min_node_num.second;
                    new_node.move_count = temp_node.move_count + 1;                    
                    new_node.huristic = huristic_function(new_puzzle);
                    new_node.zero_position = find_zeros_position(new_puzzle);
                    new_node.puzzle = new_puzzle;
                    new_node.direction_from_previous = nms;
                    
                    // printf("%d, %d\n", new_node.move_count, new_node.huristic);
                    // print_puzzle(new_puzzle);
                                        
                    visited[new_puzzle] = 1;
                    tree_map[++node_ids] = new_node;
                    pq.push(pair<int, int>(new_node.move_count + new_node.huristic, node_ids));
                }
            }
        }
            
        /*
        printf("present_puzzle:\n");
        print_puzzle(present_puzzle);
        printf("pq top puzzle:\n");
        print_puzzle(tree_map[pq.top().second].puzzle);
        printf("move count and huristic:\n %d, %d\n",tree_map[pq.top().second].move_count, tree_map[pq.top().second].huristic);
        */
    }
    
    // to print the movement count and path
    int present_id = min_node_num.second;

    vector<int> order;
    order.push_back(present_id);
    while(present_id != 0){
        present_id = tree_map[present_id].parent_id;
        order.push_back(present_id);
    }    
    reverse(order.begin(), order.end());

    printf("%d\n",order.size()-1);
    for(auto i = order.begin() + 1; i!= order.end(); ++i)
        printf("%s\n",tree_map[*i].direction_from_previous.c_str());

    return 0;
}