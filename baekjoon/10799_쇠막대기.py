# 개선된 풀이
# 시간 복잡도: O(n)
s = input()
stack = []
result = 0
for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == "(":
            result += len(stack)
        else:
            result += 1

print(result)


# 기존 풀이
# 시간 복잡도: O(nm)?
s = input()
s = s.replace("()", "L")
stack = []
layzer = []
result = 0
for i in range(len(s)):
    if not stack and s[i] == "L":
        continue

    if not stack:
        cnt_L = 0
        stack.append(s[i])
        layzer.append(1)
    elif s[i] == "L":
        cnt_L += 1
    elif s[i] == "(":
        stack.append(s[i])
        if cnt_L > 0:
            for j in range(len(layzer)):
                layzer[j] += cnt_L
            cnt_L = 0
        layzer.append(1)
    elif s[i] == ")":
        stack.pop()
        result += layzer.pop() + cnt_L
        if cnt_L > 0:
            for j in range(len(layzer)):
                layzer[j] += cnt_L
            cnt_L = 0

print(result)