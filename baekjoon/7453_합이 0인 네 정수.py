import sys
input = sys.stdin.readline

n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]

arr_1 = [0] * (n**2)
arr_2 = [0] * (n**2)
idx = 0

for i in range(n):
    for j in range(n):
        arr_1[idx] = L[i][0] + L[j][1]
        arr_2[idx] = L[i][2] + L[j][3]
        idx += 1

arr_1.sort()
arr_2.sort()

print(arr_1)
print(arr_2)