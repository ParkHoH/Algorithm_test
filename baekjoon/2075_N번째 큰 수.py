import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    for i in list(map(int, input().split())):
        heapq.heappush(heap, i)
        if len(heap) > N:
            heapq.heappop(heap)

print(heap[0])


# 메모리 초과
# import heapq
# import sys
# input = sys.stdin.readline

# N = int(input())
# L = []
# heap = []

# for _ in range(N):
#     L.append(list(map(int, input().split())))

# for i in range(N):
#     heap.append([-L[-1][i], i, N-1])

# heapq.heapify(heap)
# cnt = 0
# while cnt < N:
#     num, i, floor = heapq.heappop(heap)
#     heapq.heappush(heap, [-L[i][floor-1], i, floor-1])
#     cnt += 1

# print(-num)
