def solution(new_id):
    
    # 1단계
    new_id = str.lower(new_id)
    
    # 2단계
    must_2 = [chr(i) for i in range(ord("a"), ord("z")+1)]\
            +[str(i) for i in range(10)] + ["-", "_","."]    
    new_id = "".join([i for i in new_id if i in must_2])
    
    # 3단계
    new_id = list(new_id)
    first_visit = 1
    for i in range(len(new_id)):
        if first_visit == 1 and new_id[i] == ".":
            first_visit = 0
        
        elif first_visit == 0 and new_id[i] == ".":
            new_id[i] = ""
            
        elif first_visit == 0 and new_id[i] != ".":
            first_visit = 1
        
    new_id = "".join(new_id)
    
    # 4단계
    new_id = list(new_id)
    if new_id[0] == ".":
        new_id[0] = ""
    if new_id[-1] == ".":
        new_id[-1] = ""
    new_id = "".join(new_id)
    
    # 5단계
    if new_id == "":
        new_id = "a"
        
    # 6단계
    if len(new_id)>= 16:
        new_id = new_id[:15]
    
    new_id = list(new_id)
    if new_id[-1] == ".":
        new_id[-1] = ""
    new_id = "".join(new_id)
    
    # 7단계
    if len(new_id)<=2:
        while len(new_id) !=3:
            new_id += new_id[-1]
    
    return new_id