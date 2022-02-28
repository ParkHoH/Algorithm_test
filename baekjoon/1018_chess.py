N, M = map(int, input().split())
L = []

for _ in range(N):
    L.append(input())

WB = 'WBWBWBWB'
BW = 'BWBWBWBW'
list_1 = [WB, BW, WB, BW, WB, BW, WB, BW]
list_2 = [BW, WB, BW, WB, BW, WB, BW, WB]
result = float('inf')

for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for k in range(8):
            for l in range(8):
                if L[i+k][j+l] != list_1[k][l]:
                    cnt += 1
        result = min(result, cnt)

        cnt = 0
        for k in range(8):
            for l in range(8):
                if L[i+k][j+l] != list_2[k][l]:
                    cnt += 1
        result = min(result, cnt)

print(result)