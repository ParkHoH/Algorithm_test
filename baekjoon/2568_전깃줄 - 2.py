from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
lines = []

for _ in range(n):
    a, b = map(int, input().split())
    lines.append([a, b])

lines.sort()
stack = []
cost = []

for line in lines:
    if not stack or stack[-1] < line[1]:
        stack.append(line[1])
        cost.append([len(stack), line[0]])
    
    else:
        idx = bisect_left(stack, line[1])
        stack[idx] = line[1]
        cost.append([idx+1, line[0]])

idx = len(stack)
result = []

for i in range(n-1, -1, -1):
    if cost[i][0] == idx:
        idx -= 1
    else:
        result.append(cost[i][1])

result.sort()

print(len(result))
for i in result:
    print(i)