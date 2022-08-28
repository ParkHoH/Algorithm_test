import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    result = 0

    while len(files) >= 2:
        new_file = heapq.heappop(files) + heapq.heappop(files)
        result += new_file
        heapq.heappush(files, new_file)

    print(result)