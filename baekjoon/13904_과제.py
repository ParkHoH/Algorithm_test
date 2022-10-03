import heapq
import sys
input = sys.stdin.readline

N = int(input())
tasks = [list(map(int, input().split())) for _ in range(N)]
tasks.sort(reverse=True)

heap = []
cur_day = tasks[0][0]
answer = 0

for limit_day, score in tasks:
    if limit_day == cur_day:
        heapq.heappush(heap, -score)
        continue

    while limit_day != cur_day:
        cur_day -= 1
        if heap: answer -= heapq.heappop(heap)

    heapq.heappush(heap, -score)

while heap and cur_day > 0:
    cur_day -= 1
    answer -= heapq.heappop(heap)

print(answer)