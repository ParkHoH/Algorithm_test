TC = int(input())
for _ in range(TC):
    string = input()
    stack = []
    dic = {"(": ")", ")": "("}

    for s in string:
        if not stack:
            stack.append(s)
            if s == ")":
                break

        elif dic[stack[-1]] != s:
            stack.append(s)
        else:
            stack.pop()

    if stack:
        print("NO")
    else:
        print("YES")
