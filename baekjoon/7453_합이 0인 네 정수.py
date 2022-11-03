from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
L = [tuple(map(int, input().split())) for _ in range(n)]

dic = {}
# dic = defaultdict(int) # defaultdict가 더 느릴 수 있음
idx = 0

for i in range(n):
    for j in range(n):
        num = L[i][0] + L[j][1]
        # dic[num] += 1
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

answer = 0

for i in range(n):
    for j in range(n):
        num = L[i][2] + L[j][3]

        if -num in dic:
            answer += dic[-num]

print(answer)