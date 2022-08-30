import heapq
import sys
input = sys.stdin.readline

N = int(input())
left_heap = []
right_heap = []

for _ in range(N):
    num = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    if right_heap and -left_heap[0] > right_heap[0]:
        min_value = heapq.heappop(right_heap)
        max_value = -heapq.heappop(left_heap)

        heapq.heappush(left_heap, -min_value)
        heapq.heappush(right_heap, max_value)

    print(-left_heap[0])