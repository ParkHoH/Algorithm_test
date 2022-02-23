N, M = map(int, input().split())
list_num = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_ijk = list_num[i] + list_num[j] + list_num[k]
            if sum_ijk <= M and list_num[i] + sum_ijk > result:
                result = sum_ijk

print(result)