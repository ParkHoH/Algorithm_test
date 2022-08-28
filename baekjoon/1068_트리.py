import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))
k = int(input())

graph = [[] for _ in range(n)]
start = k

for i in range(n):
    root = L[i]
    if i == k or root == k:
        continue

    if root == -1:
        start = i
    else:
        graph[root].append(i)

result = 0

def dfs(idx):
    if graph[idx]:
        for i in graph[idx]:
            dfs(i)

    else:
        global result
        result += 1

if k != start:
    dfs(start)

print(result)


# import sys
# input = sys.stdin.readline

# def dfs(num, L):
#     L[num] = -2
#     for i in range(len(L)):
#         if num == L[i]:
#             dfs(i, L)

# n = int(input())
# L = list(map(int, input().split()))
# k = int(input())
# cnt = 0

# dfs(k, L)
# cnt = 0
# for i in range(len(L)):
#     if L[i] != -2 and i not in L:
#         cnt += 1
# print(cnt)