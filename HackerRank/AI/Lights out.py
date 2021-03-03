import sys
import random
import math
import copy

def SMCTS(map_):
    answer = [0, 0]
    answer_sample = []
    win_rate = []
    for i in range(len(map_)):
        for j in range(len(map_[i])):
            if map_[i][j]=='1':
                answer_sample.append([i,j])
                win_rate.append([0,0])
    
    simulation_time = int(len(win_rate) / 4 * 100)
    for t in range(1,simulation_time):
        cmap = copy.deepcopy(map_)
        index = selection_function(win_rate, (t-1)*4+1)
        win_rate[index][0] += game_play(cmap, answer_sample[index][0],answer_sample[index][1],'random')        
        win_rate[index][1] += 1
        
        cmap = copy.deepcopy(map_)
        index = selection_function(win_rate, (t-1)*4+2)
        win_rate[index][0] += game_play(cmap, answer_sample[index][0],answer_sample[index][1],'front')        
        win_rate[index][1] += 1
                
        cmap = copy.deepcopy(map_)
        index = selection_function(win_rate, (t-1)*4+3)
        win_rate[index][0] += game_play(cmap, answer_sample[index][0],answer_sample[index][1],'back')        
        win_rate[index][1] += 1     
        
        cmap = copy.deepcopy(map_)
        index = selection_function(win_rate, (t-1)*4+4)
        win_rate[index][0] += game_play(cmap, answer_sample[index][0],answer_sample[index][1],'many')        
        win_rate[index][1] += 1
    
    total_win_rate = list(map(lambda x:x[0]/(x[1]+0.00001),win_rate))
    answer = answer_sample[total_win_rate.index(max(total_win_rate))]
    if max(total_win_rate) == 0:
        answer = answer_sample[random.randrange(len(answer_sample))]
        
    print(total_win_rate)
    return answer

def selection_function(win_rate, t):
    probability = []
    for i in win_rate:
        if i[1]==0:
            probability.append(1)
        else:
            probability.append(i[0]/i[1]+math.sqrt(2*(math.log(t)+1)/i[1]))
    
    sum_ = sum(probability)
    prob = list(map(lambda x: x/sum_, probability))
    
    c_prob = [prob[0]]
    for i in range(1,len(prob)):
        c_prob.append(prob[i]+c_prob[i-1])
        
    dart = random.random()
    for i in range(len(c_prob)):
        if dart < c_prob[i]:
            return i
        
    del probability
    del prob
    del c_prob
    return 0

def game_play(map_,i,j,policy):    
    map_change(map_,i,j)
    
    for _ in range(49):
        answer_sample1 = []
        answer_sample2 = []
        for i in range(len(map_)):
            for j in range(len(map_[i])):
                if map_[i][j]=='1':
                    answer_sample1.append([i,j])
                    
        if answer_sample1 == []:
            return 1
        
        if policy == "random":
            enemy_select = answer_sample1[random.randrange(len(answer_sample1))]
        elif policy == "front":
            enemy_select = answer_sample1[0]
        elif policy == "back":
            enemy_select = answer_sample1[len(answer_sample1)-1]
        elif policy == "many":
            enemy_select = many_neighbor(answer_sample1, map_)
            
        map_change(map_, enemy_select[0], enemy_select[1])
                
        for i in range(len(map_)):
            for j in range(len(map_[i])):
                if map_[i][j]=='1':
                    answer_sample2.append([i,j])
                
        if answer_sample2 == []:
            return 0
        my_select = answer_sample2[random.randrange(len(answer_sample2))]
        map_change(map_,my_select[0],my_select[1])
        
    return 0

def map_change(map_,i,j):    
    map_[i][j] = '0'
    try: 
        if map_[i+1][j] == '0':
            map_[i+1][j] = '1'
        else:
            map_[i+1][j] = '0'
    except:
        pass
    
    try: 
        if map_[i][j+1] == '0':
            map_[i][j+1] = '1'
        else:
            map_[i][j+1] = '0'
    except:
        pass

def many_neighbor(sample, map_):
    number = -1
    select = sample[0]
    for one in sample:
        i = one[0]
        j = one[1]
        try:
            count = int(map_[i][j])+int(map_[i+1][j])+int(map_[i][j+1])
        except:
            try:
                count = int(map_[i][j])+int(map_[i+1][j])
            except:
                try:
                    count = int(map_[i][j])+int(map_[i][j+1])
                except:
                    count = int(map_[i][j])
        
        if number < count:
            number = count
            select = one       
    
    return select
    
    
if __name__ == "__main__":
    player = int(input())
    
    rmap_ = []
    for i in sys.stdin:
        rmap_.append(str(i[:-1]))
    map_ = [list(i) for i in rmap_]
    print(map_)
    select = SMCTS(map_)
    
    print(select[0], select[1])