n = int(input())
L = list(map(int, input().split()))

L.sort()
start, end = 0, n-1
answer = []
abs_sum = float('inf')
while start < end:
    if abs(L[start] + L[end]) < abs_sum:
        answer = [L[start], L[end]]
        abs_sum = abs(L[start] + L[end])

    if L[start] + L[end] == 0:
        break
    elif L[start] + L[end] > 0:
        end -= 1
    else:
        start += 1

print(answer[0], answer[1])