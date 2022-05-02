N = int(input())
L = list(map(int, input().split()))
start = 0
end = len(L)-1
min_value = float('inf')
while start < end:
    value = L[start] + L[end]
    if min_value > abs(value):
        min_value = abs(value)
        result = [L[start], L[end]]

    if value == 0:
        break
    elif value > 0:
        end -=1
    else:
        start += 1

for i in result:
    print(i, end=" ")