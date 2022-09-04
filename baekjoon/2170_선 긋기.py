import sys
input = sys.stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]

lines.sort(key=lambda x: [x[0], x[1]])
result = 0
start, end = lines[0]

for i in range(1, N):
    new_start, new_end = lines[i]

    if new_start <= end:
        end = max(end, new_end)
    else:
        result += end-start
        start, end = lines[i]

result += end-start
print(result)