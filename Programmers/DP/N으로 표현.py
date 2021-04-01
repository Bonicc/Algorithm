def solution(N, number):
    sets = [set() for _ in range(8)]
    for i in range(8):
        sets[i].add(int(''.join([str(N) for _ in range(i+1)])))
        for j in range(i):
            for number1 in sets[j]:
                for number2 in sets[i-j-1]:
                    if number1+number2 <=32000:
                        sets[i].add(number1+number2)
                    if number1-number2 > 1:
                        sets[i].add(number1-number2)
                    if number1*number2 <=32000:
                        sets[i].add(number1*number2)
                    if number2!=0:
                        sets[i].add(number1//number2)
    for i in range(8):
        if number in sets[i]:
            return i+1
    return -1