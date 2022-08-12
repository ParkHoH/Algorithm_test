N = int(input())
M = int(input())
S = input()

cnt_IOI = 0
idx = 0
result = 0

while idx < M:
    if S[idx:idx+3] == "IOI":
        cnt_IOI += 1
        idx += 2

        if cnt_IOI == N:
            cnt_IOI -= 1
            result += 1

    else:
        cnt_IOI = 0
        idx += 1
    
print(result)


# 50점: 시간 초과
N = int(input())
M = int(input())
S = input()

P = "IO" * N + "I"
cnt = 0
len_p = len(P)

for i in range(M - (2*N + 1)):
    if S[i:i+len_p] == P:
        cnt += 1

print(cnt)