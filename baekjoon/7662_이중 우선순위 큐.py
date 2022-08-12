import heapq
import sys
input = sys.stdin.readline

T = int(input())
exist = [False] * (1000001)

for _ in range(T):
    k = int(input())
    max_heap = []
    min_heap = []

    for key in range(k):
        oper = input().split()
        oper[1] = int(oper[1])
        if oper[0] == "I": # 삽입 연산
            heapq.heappush(max_heap, [-oper[1], key])
            heapq.heappush(min_heap, [oper[1], key])
            exist[key] = True

        else: # 삭제 연산
            if oper[1] == 1: # 최대값 제거
                while max_heap and not exist[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                
                if max_heap:
                    exist[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            else: # 최소값 제거
                while min_heap and not exist[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                
                if min_heap:
                    exist[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while max_heap and not exist[max_heap[0][1]]:
        heapq.heappop(max_heap)

    while min_heap and not exist[min_heap[0][1]]:
        heapq.heappop(min_heap)
        
    if max_heap:
        print(-max_heap[0][0], end=" ")
        print(min_heap[0][0])
    else:
        print("EMPTY")


# 시간 초과
# import heapq
# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     k = int(input())
#     max_heap = []
#     min_heap = []

#     for _ in range(k):
#         oper = input().split()
#         oper[1] = int(oper[1])
#         if oper[0] == "I": # 삽입 연산
#             heapq.heappush(max_heap, -oper[1])
#             heapq.heappush(min_heap, oper[1])

#         else: # 삭제 연산
#             if not max_heap:
#                 continue

#             if oper[1] == 1: # 최대값 제거
#                 num = -heapq.heappop(max_heap)

#                 for i in range(len(min_heap)):
#                     if min_heap[i] == num:
#                         del min_heap[i]
#                         break

#                 heapq.heapify(min_heap)

#             else: # 최소값 제거
#                 num = -heapq.heappop(min_heap)

#                 for i in range(len(max_heap)):
#                     if max_heap[i] == num:
#                         del max_heap[i]
#                         break

#                 heapq.heapify(max_heap)

#     if max_heap:
#         print(-heapq.heappop(max_heap), end=" ")
#         print(heapq.heappop(min_heap))
#     else:
#         print("EMPTY")