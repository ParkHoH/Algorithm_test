# stack solution
def solution(s):
    stack = []
    for alphabet in s:
        if not stack:
            stack.append(alphabet)
        else:
            if stack[-1] == alphabet:
                stack.pop()
            else:
                stack.append(alphabet)
    return 0 if stack else 1


# 시간 초과 solution
def solution(s):
    set_s = list(set(s))
    while s:
        stop = True
        for alphabet in set_s:
            if alphabet*2 in s:
                s = s.replace(alphabet*2, '') # 시간 초과 발생 원인
                stop = False
                break
        if stop:
            return 0
    return 1

print(solution("abbcdaaadca"))