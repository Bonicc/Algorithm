def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    i,j = 0, len(people)-1
    try:
        while i <= j:
            speople = 0
            while people[i] + speople <= limit:
                speople += people[i]
                i+=1
            while people[j] + speople <= limit:
                speople += people[j]
                j-=1
            answer += 1
    except:
        answer += 1
    return answer