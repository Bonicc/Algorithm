def solution(phone_book):
    answer = True
    sort_index = sorted(list(enumerate(map(lambda x: len(x),phone_book))),key = lambda x:x[1])
    sorted_pb = []
    for i in range(len(sort_index)):
        if i==0 :
            sorted_pb.append(phone_book[sort_index[0][0]])
            continue
        for j in range(len(sorted_pb)):
            if sorted_pb[j] == phone_book[sort_index[i][0]][:sort_index[j][1]]:
                return False
        sorted_pb.append(phone_book[sort_index[i][0]])
        
    return answer