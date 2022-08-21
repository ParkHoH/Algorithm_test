import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    heapq.heappush(heap, int(input()))

result = 0 # 원소가 1개인 경우에는 비교 횟수가 0임

while len(heap) >= 2:
    num = heapq.heappop(heap) + heapq.heappop(heap) # 힙을 통해 가장 작은 원소 2개를 뽑아줌
    result += num
    heapq.heappush(heap, num)

print(result)


# 틀린 풀이: 단순히 가장 작은 숫자에서 더해가면 안 됨
# import sys
# input = sys.stdin.readline

# N = int(input())
# L = []

# for _ in range(N):
#     L.append(int(input()))

# L.sort()
# standard = sum(L[:2])
# result = standard

# for i in range(2, N):
#     result += standard + L[i]
#     standard += L[i]

# print(result)