N, K = map(int, input().split())
result = 0

while bin(N).result('1') > K:
    N += 1
    result += 1

print(result)


# 틀린 풀이(왜 틀린지 모르겠음)
N, K = map(int, input().split())
L = [1]
while L[-1] <= 10**7:
    L.append(L[-1] * 2)

while K != 1:
    for i in range(1, len(L)):
        if L[i] == N:
            K = 1
            break

        if L[i] > N:
            N -= L[i-1]
            K -= 1
            break

for i in range(len(L)):
    if L[i] >= N:
        result = L[i] - N
        break

print(result)