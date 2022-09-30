import heapq
import sys
input = sys.stdin.readline

N = int(input())
lectures = sorted([list(map(int, input().split())) for _ in range(N)])
heap = []

for start, end in lectures:
    if heap and heap[0] <= start: heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap))


# 틀린 풀이
# from collections import defaultdict
# import sys
# input = sys.stdin.readline

# N = int(input())
# lectures = [list(map(int, input().split())) for _ in range(N)]
# lectures.sort()

# answer = 0
# dic = defaultdict(int)

# for start, end in lectures:
#     if dic[start] != 0:
#         dic[start] -= 1
#         dic[end] += 1
    
#     else:
#         answer += 1
#         dic[end] += 1

# print(answer)