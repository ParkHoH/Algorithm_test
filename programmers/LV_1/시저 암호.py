#my solution
from re import S


def solution(s, n):
    result = list(map(ord, s))

    for i in range(len(result)):
        if result[i] != 32:
            if result[i] >= 65 and result[i] <= 90:
                if result[i] + n > 90:
                    result[i] = result[i] + n - 26
                else:
                    result[i] = result[i] + n
            else:
                if result[i] + n > 122:
                    result[i] = result[i] + n - 26
                else:
                    result[i] = result[i] + n
            
    return ''.join(map(chr, result))

#better code
def solution(s, n):
    s = list(s)

    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord("A") + n) % 26 + ord("A")) 
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord("a") + n) % 26 + ord("a"))

    return ''.join(s)

print(solution("a B z", 4))