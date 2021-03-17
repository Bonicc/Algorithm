def solution(food_times, k):
    answer = 0
    times = sorted(food_times)
    food_diction = dict()
    for i in times:
        try: food_diction[i] += 1
        except: food_diction[i] = 1
    
    prev_i = 0
    left_food = len(food_times)    
    for i in food_diction:
        if left_food*(i-prev_i) <= k:
            k -= left_food*(i-prev_i)
            left_food -= food_diction[i]
            prev_i = i
        else:
            break
    if left_food == 0:
        return -1
    
    index = k % left_food 
    after_limit_times = [i-prev_i for i in food_times]
    j = -1
    for i in range(len(food_times)):
        if after_limit_times[i] > 0:
            j += 1
        if index == j:
            return i+1