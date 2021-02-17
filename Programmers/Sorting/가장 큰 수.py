def solution(numbers):
    return str(int("".join(list(map(lambda x: str(x), sorted(numbers,reverse = True, key = lambda x: (str(x)*4)[0:4]))))))