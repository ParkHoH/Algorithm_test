n = int(input())
L = list(map(int, input().split()))
x = int(input())

L.sort()
start, end = 0, n-1
answer = 0
while start < end:
    if L[start] + L[end] == x:
        answer += 1
        start += 1
        end -= 1
    elif L[start] + L[end] > x:
        end -= 1
    else:
        start += 1

print(answer)