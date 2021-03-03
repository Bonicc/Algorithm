def solution(number, k):
    stack = [number[0]]
    for i in range(1, len(number)):
        try:
            while int(stack[-1]) < int(number[i]):
                stack.pop()
                k -= 1
                if k == 0:
                    break
        except:
            pass
                
        if k == 0:
            for j in range(i, len(number)):
                stack.append(number[j])            
            break
        else:
            stack.append(number[i])
    if k != 0:
        return ''.join(stack[:-k])
    else:
        return ''.join(stack)