# 그리디 문제
N, K = map(int, input().split())
nums = list(input())
k, stack = K, []

for num in nums:
    while k > 0 and stack and stack[-1] < num:
        stack.pop()
        k -= 1
    
    stack.append(num)

print(''.join(stack[:N-K]))

# 오답 풀이
# N, K = map(int, input().split())
# nums = list(input())

# result = []
# standard = []
# idx = 0
# cnt_removed = 0

# while True:
#     # if idx >= N or len(result) + len(standard) + (N-idx) == N-K:
#     if cnt_removed == K or N-K == len(result) + len(standard) + (N-idx):
#         result += standard + nums[idx:]
#         break

#     if not standard:
#         standard.append(nums[idx])
#         idx += 1

#     else:
#         if int(standard[0]) < int(nums[idx]):
#             standard.pop()
#             cnt_removed += 1
#             standard.append(nums[idx])
#             idx += 1
        
#         else:
#             result.append(standard[0])
#             standard = []


# print(''.join(result))