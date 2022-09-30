import heapq
import sys
input = sys.stdin.readline

N = int(input())
tasks = [list(map(int, input().split())) for _ in range(N)]
tasks.sort(reverse=True)

day = tasks[0][0] 
answer = 0
heap = []

for task in tasks:
    heapq.heappush(heap, -task[1])

    while heap and day != 0 and day != task[0]:
        answer += heapq.heappop(heap)
        day -= 1

print(-answer)