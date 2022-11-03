import heapq

N, L = map(int, input().split())
A = list(map(int, input().split()))
heap = []

for i in range(N):
    if i - L >= 0:
        while heap and heap[0][1] <= i-L:
            heapq.heappop(heap)

    heapq.heappush(heap, (A[i], i))
    print(heap[0][0], end=" ")