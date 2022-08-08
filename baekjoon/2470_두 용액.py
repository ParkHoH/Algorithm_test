n = int(input())
L = list(map(int, input().split()))

L.sort()
start, end = 0, n-1
result = []
sum_value = float('inf')
while start < end:
    if abs(L[start] + L[end]) < sum_value:
        result = [L[start], L[end]]
        sum_value = abs(L[start] + L[end])

    if L[start] + L[end] == 0:
        break
    elif L[start] + L[end] > 0:
        end -= 1
    else:
        start += 1

print(result[0], result[1])