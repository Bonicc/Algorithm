import sys

import heapq as hq
import copy

def board_check(board, answer): 
    # check the present board's incorrectness (hueristic function value)
    result = 0
    for bs, ans in zip(board, answer):
        for b,a in zip(bs,ans):
            result += 1 * (b!=a)
    return result

def board_flatten(board): 
    # get the tuple of board
    return tuple(sum(board,[]))

def astar_puzzle(board, start_position):
    board_size = len(board[0])
    answer_board = [[3*i+j for j in range(board_size)] for i in range(board_size)]
    movement = {"up": [-1,0], "down":[1,0],"left":[0,-1],"right":[0,1]}
    
    tree = {}
    board_tree = {}
    
    node_id= 0   # node id
    start_g = 0      # move count
    start_h = board_check(board, answer_board)  # board incorrenctness
    start_f = start_g + start_h  # sum of g, h
    
    # node = [[0]f, [1]g, [2]h, [3]board, [4]position, [5]node_id, [6]parent_id, [7]direction_from_parent] 
    start_node = [start_f, start_g, start_h, board, start_position, node_id, None, None]
    
    pq = [start_node]
    tree[start_node[5]] = start_node
    board_tree[board_flatten(board)] = start_f
    
    while pq:
        node = hq.heappop(pq)
        if node[2] == 0: # if board is answer board
            final_node = node
            break
        
        g = node[1] + 1
        
        parent_id = node[5]
        position = node[4] 
        
        for m in movement:
            next_position = list(map(lambda x,y: x+y, position, movement[m]))
            if not (next_position[0]>=0 and next_position[0] < board_size and next_position[1]>=0 and next_position[1] < board_size):
                continue
            
            c_board = copy.deepcopy(node[3])
            c_board[position[0]][position[1]], c_board[next_position[0]][next_position[1]] = \
            c_board[next_position[0]][next_position[1]], c_board[position[0]][position[1]]
            
            h = board_check(c_board, answer_board)
            f = g + h
                        
            # If there is board which is already experienced, skip the board if it has higher f value
            try:
                board_tree[board_flatten(c_board)] = min(board_tree[board_flatten(c_board)], f)
                continue
            except:
                board_tree[board_flatten(c_board)] = f
                
            node_id += 1
            next_node = [f, g, h, c_board, next_position, node_id, parent_id, m.upper()]
            
            hq.heappush(pq, next_node)            
            tree[node_id] = next_node    
    
    return tree, final_node

if __name__ == "__main__":
    board_size = int(sys.stdin.readline())
    board = [[int(sys.stdin.readline()) for _ in range(board_size)]for _ in range(board_size)]
    
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                start_position = [i,j]
                
    tree, final_node = astar_puzzle(board, start_position)
    
    answer = []
    answer_board = []
    node = final_node
    while node[6] != None:
        answer.append(node[-1])
        node = tree[node[-2]]
        
    answer = list(reversed(answer))    
    print(len(answer))
    for a in answer:
        print(a)