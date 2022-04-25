# better solution
s = input().split("-")
result = 0
for i in range(len(s)):
    for j in s[i].split("+"):
        result += -int(j) if i else int(j)
print(result)


# regular expression solution
import re

s = input()
s = re.findall('(\d+)+([-+])?', s)
i = 0
while i < len(s):
    if s[i][1] == "+":
        s[i] = (str(int(s[i][0]) + int(s[i+1][0])), s[i+1][1])
        s = s[:i+1] + s[i+2:]
    else:
        i += 1

result = int(s[0][0])
for i in range(1, len(s)):
    result -= int(s[i][0])

print(result)


# 처음에 0이 연속으로 나타나지 않을 경우 가능한 풀이임
s = input().split("-")
result = s[0]
for i in range(1, len(s)):
    result += "-(" + s[i] + ")"
print(eval("result"))