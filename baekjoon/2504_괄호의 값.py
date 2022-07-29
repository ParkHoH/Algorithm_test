# 미완성, 조금 더 고민해보기
s = input()
result = ""
stack = []
dic = {
    ")": "(", 
    "(": "2", 
    "]": "[", 
    "[": "3"
    }

for i in range(len(s)):
    if not stack:
        stack.append(s[i])
    else:
        if stack[-1] == dic[s[i]]:
            poped = stack.pop()
            

    if s[i] == dic[s[i+1]]:
        poped = stack.pop()
        result = dic[poped] + "+" + "(" + result + ")"
    
    else:
        stack.append(s[i])
        result = dic[s[i]] + "*" + "(" + result + ")"