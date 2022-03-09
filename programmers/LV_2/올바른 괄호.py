def solution(s):
    cnt = 0
    if (s[0] == "(" and s[-1] == ")") and (s.count("(") == s.count(")")):
        for i in range(len(s)):
            cnt = cnt + 1 if s[i] == "(" else cnt - 1
            if cnt < 0:
                return False
        return True
    else:
        return False

print(solution("())(()"))