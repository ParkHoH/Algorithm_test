import sys
input = sys.stdin.readline

def dfs(num, L):
    L[num] = -2
    for i in range(len(L)):
        if num == L[i]:
            dfs(i, L)

n = int(input())
L = list(map(int, input().split()))
k = int(input())
cnt = 0

dfs(k, L)
cnt = 0
for i in range(len(L)):
    if L[i] != -2 and i not in L:
        cnt += 1
print(cnt)