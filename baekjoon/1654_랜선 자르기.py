import sys
input = sys.stdin.readline

K, N = map(int, input().split())
L = []
for _ in range(K):
    L.append(int(input()))

start = 0
end = 2**31 - 1
while start <= end:
    mid = (start + end) // 2
    num = 0
    for i in L:
        num += i // mid

    if num >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)