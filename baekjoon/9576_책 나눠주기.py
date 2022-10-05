# x[1] 기준 오름차순 정렬
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    wants = [[*map(int, input().split())] for _ in range(M)]

    wants.sort(key=lambda x: x[1]) # 다른 기준으로 정렬할 경우에는 항상 반례가 존재함
    rented = [False] * (N+1)
    answer = 0
    
    for start, end in wants:
        for i in range(start, end+1):
            if not rented[i]:
                rented[i] = True
                answer += 1
                break

    print(answer)


# 틀린 풀이 : 오름차순으로 정렬할 떄 오류 발생
# 반례:
# 3 3
# 1 3 
# 1 1
# 2 2
# import sys
# input = sys.stdin.readline

# def find(x, parent):
#     if x != parent[x]:
#         parent[x] = find(parent[x], parent)

#     return parent[x]

# for _ in range(int(input())):
#     N, M = map(int, input().split())

#     wants = [[*map(int, input().split())] for _ in range(M)]
#     wants.sort(key=lambda x: (x[0], x[1]))

#     answer = 0
#     parent = [i for i in range(N+1)]

#     for start, end in wants:
#         if start > N or answer == N: break
#         if parent[start] > N: continue

#         parent_start = find(start, parent)

#         if parent_start <= end: 
#             parent[parent_start] += 1
#             answer += 1

#     print(answer)