import heapq
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = deque(sorted([list(map(int, input().split())) for _ in range(N)]))
bags = [int(input()) for _ in range(K)]

bags.sort()
poped_jewel = []
result = 0

for bag in bags:
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(poped_jewel, -jewels.popleft()[1])

    if poped_jewel:
        result += -heapq.heappop(poped_jewel)

print(result)


# 힙으로만 구현
import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

heapq.heapify(jewels)
bags.sort()
poped_jewel = []
result = 0

for bag in bags:
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(poped_jewel, -heapq.heappop(jewels)[1])

    if poped_jewel:
        result += -heapq.heappop(poped_jewel)

print(result)