def solution(s):
    result = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            string = s[i:j]
            if len(string) > result and string == string[::-1]:
                result = len(string)
    
    return result