from collections import deque

n, k = map(int, input().split())
L = set([int(input()) for _ in range(n)])
dp = [-1] * (k+1)
queue = deque()
queue.append([0, 0])

while queue:
    num, cnt = queue.popleft()
    for i in L:
        if num+i > k:
            continue

        if dp[num+i] == -1:
            dp[num+i] = cnt+1
            queue.append([num+i, cnt+1])

print(dp[-1])