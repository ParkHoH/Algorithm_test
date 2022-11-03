import sys
input = sys.stdin.readline

N, C = map(int, input().split())
home = [int(input()) for _ in range(N)]
home.sort()

start, end = 0, home[-1]

while start <= end:
    mid = (start + end) // 2
    standard = home[0]
    cnt = 1

    for i in range(1, N):
        if home[i] - standard >= mid:
            cnt += 1
            standard = home[i]

    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1

print(start-1)