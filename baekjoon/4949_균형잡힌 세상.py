import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == ".":
        break
    
    result = "yes"
    dic = {"(": ")", "[": "]"}
    stack = []

    for s in string:
        if s == "(" or s == "[":
            stack.append(s)

        elif s == ")" or s == "]":
            if stack and dic[stack[-1]] == s:
                stack.pop()
            else:
                result = "no"
                break

    if stack:
        print("no")
    else:
        print(result)