def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        try:
            if participant[i]!=completion[i]:
                answer = participant[i]
                break
        except:
            answer = participant[i]
            break
    return answer