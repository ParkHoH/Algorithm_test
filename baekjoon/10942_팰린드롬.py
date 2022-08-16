import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for start in range(n - i):
        end = start + i
        
        if start == end:
            dp[start][end] = 1
        elif numbers[start] == numbers[end]:
            if start + 1 == end: 
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1: 
                dp[start][end] = 1
            
for question in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])

# import sys
# input = sys.stdin.readline


# def mark(ori_start, start, ori_end, num):
#     if ori_start == start:
#         dp[ori_start][ori_end] = num
#         dp[ori_end][ori_start] = num
#         return

#     for i in range(start-ori_start):
#         if dp[i][ori_end-i] != -1:
#             break
        
#         dp[ori_start+i][ori_end-i] = num
#         dp[ori_end-i][ori_start+i] = num


# N = int(input())
# num = input().split()
# dp = [[-1] * N for _ in range(N)]
# M = int(input())

# for _ in range(M):
#     ori_start, ori_end = map(int, input().split())
#     ori_start -= 1
#     ori_end -= 1
#     start, end = ori_start, ori_end
#     result = 1

#     while start <= end:
#         if dp[start][end] != -1:
#             result = dp[start][end]
#             break

#         if num[start] == num[end]:
#             start += 1
#             end -= 1
#         else:
#             result = 0
#             break
    
#     mark(ori_start, start, ori_end, result)
#     print(result)
