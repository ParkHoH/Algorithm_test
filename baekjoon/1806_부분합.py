# 굳이 정렬할 필요 없는 문제임
N, S = map(int, input().split())
L = list(map(int, input().split()))

answer = N+1
start = end = 0
sum_ele = 0
while end < N:
    sum_ele += L[end]
    if sum_ele >= S:
        while start <= end:
            answer = min(end-start+1, answer)
            if sum_ele - L[start] < S:
                break
            sum_ele -= L[start]
            start += 1
    end += 1

if answer == N+1:
    print(0)
else:
    print(answer)