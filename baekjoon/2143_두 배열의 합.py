from bisect import bisect_left, bisect_right

T = int(input())
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

sum1 = []
sum2 = []

for i in range(n):
    sum_value = arr1[i]
    sum1.append(sum_value)
    for j in range(i+1, n):
        sum_value += arr1[j]
        sum1.append(sum_value)

for i in range(m):
    sum_value = arr2[i]
    sum2.append(sum_value)
    for j in range(i+1, m):
        sum_value += arr2[j]
        sum2.append(sum_value)

sum1.sort()
sum2.sort()
result = 0

for i in sum1:
    result -= bisect_left(sum2, T-i)
    result += bisect_right(sum2, T-i)

print(result)


# # 메모리 초과 (pypy로는 통과함)
# from collections import defaultdict

# T = int(input())
# n = int(input())
# arr1 = list(map(int, input().split()))
# m = int(input())
# arr2 = list(map(int, input().split()))

# dic1 = defaultdict(int)
# dic2 = defaultdict(int)

# for i in range(n):
#     sum_value = arr1[i]
#     dic1[sum_value] += 1
#     for j in range(i+1, n):
#         sum_value += arr1[j]
#         dic1[sum_value] += 1

# for i in range(m):
#     sum_value = arr2[i]
#     dic2[sum_value] += 1
#     for j in range(i+1, m):
#         sum_value += arr2[j]
#         dic2[sum_value] += 1

# result = 0

# for k, v in dic1.items():
#     result += v * dic2[T-k]

# print(result)
