N = int(input())
L = list(map(int, input().split()))
L.sort()
if L[0] > 0:
    for i in range(3):
        print(L[i], end=" ")
elif L[-1] < 0:
    for i in range(3):
        print(L[-(3-i)], end=" ")
else:
    min_value = float('inf')
    stop = False
    for i in range(len(L)-2):
        start = i+1
        end = len(L)-1
        while start < end:
            value = L[i] + L[start] + L[end]
            if min_value > abs(value):
                min_value = abs(value)
                result = [L[i], L[start], L[end]]

            if value == 0:
                stop = True
                break
            elif value > 0:
                end -=1
            else:
                start += 1
        if stop: break

    for i in result:
        print(i, end=" ")