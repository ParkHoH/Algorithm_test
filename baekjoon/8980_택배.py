from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
village = [[*map(int, input().split())] for _ in range(M)]
village.sort(key=lambda x: (x[0], x[1]))

answer = cur_box = 0
heap = []

for start, end, cnt_box in village:
    while heap and heap[0][0] == start:
        _, plus_box = heappop(heap)
        cur_box -= plus_box
        answer += plus_box

    if cur_box < C:
        possible_cnt = min(C - cur_box, cnt_box)
        cur_box += possible_cnt
        heappush(heap, [end, possible_cnt])

print(answer + sum([plus_box for _, plus_box in heap]))

# 30 40 20 60