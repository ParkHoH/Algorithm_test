def solution(s):
    dic = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }
    result = 0
    for i in range(len(s)):
        s_copy = s[i:] + s[:i]
        stack = [s_copy[0]]
        for j in range(1, len(s_copy)):
            if len(stack) > 0 and stack[-1] in dic and dic[stack[-1]] == s_copy[j]:
                stack.pop()
            else:
                stack.append(s_copy[j])
        if len(stack) == 0:
            result += 1
    return result

print(solution("[](){}"))