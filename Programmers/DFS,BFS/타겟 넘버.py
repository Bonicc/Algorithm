def solution(numbers, target):
    answer = [0]
    for i in numbers:
        new_answer = []
        for j in answer:
            new_answer.append(j-i)
            new_answer.append(j+i)
        answer = new_answer
    return answer.count(target)