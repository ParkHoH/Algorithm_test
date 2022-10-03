import heapq
import sys
input = sys.stdin.readline

# n = int(input())
# lecture = [list(map(int, input().split())) for _ in range(n)]
# lecture.sort(key=lambda x: -x[1])

# heap = []
# answer = 0
# if n != 0: cur_day = lecture[0][1]

# for pay, day in lecture:
#     if day == cur_day:
#         heapq.heappush(heap, -pay)
#         continue
    
#     while day != cur_day:
#         cur_day -= 1
#         if heap: answer -= heapq.heappop(heap)
    
#     heapq.heappush(heap, -pay)

# while heap and cur_day > 0:
#     cur_day -= 1
#     answer -= heapq.heappop(heap)

# print(answer)


# 더 효율적인 코드
n = int(input())
heap = []

for pay, day in sorted([[*map(int, input().split())] for _ in range(n)], key=lambda x: x[1]):
    heapq.heappush(heap, pay)
    if len(heap) > day: heapq.heappop(heap)

print(sum(heap))