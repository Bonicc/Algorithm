from itertools import combinations

def solution(orders, course):
    answer = []
    order_hash = [{} for i in range(11)]
    
    for c in course:
        for order in orders:
            list_order = list(order)
            for comb in combinations(list_order,c):
                comb = "".join(sorted(comb))
                try:
                    order_hash[c][comb] += 1
                except:
                    order_hash[c][comb] = 1
        
    for c in course:
        max_ = max(list(order_hash[c].values())+[2])            
        for comb in order_hash[c]:
            if order_hash[c][comb] == max_:
                answer.append("".join(comb))
    
    return sorted(answer)