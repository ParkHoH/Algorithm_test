import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
result = 0
min_list = []

if N == 1:
    L.sort()
    result += sum(L[0:5])

else:
    min_list.append(min(L[0], L[5]))
    min_list.append(min(L[1], L[4]))
    min_list.append(min(L[2], L[3]))
    
    min_list.sort()

    min_1 = min_list[0]
    min_2 = min_list[0] + min_list[1]
    min_3 = sum(min_list)

    n1 = 4 * (N - 2) * (N - 1) + (N - 2) ** 2
    n2 = 4 * (N - 1) + 4 * (N - 2)
    n3 = 4

    result += min_1 * n1
    result += min_2 * n2
    result += min_3 * n3

print(result)