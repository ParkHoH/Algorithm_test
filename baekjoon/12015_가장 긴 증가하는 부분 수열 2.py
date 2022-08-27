N = int(input())
L = list(map(int, input().split()))

result = []

for i in L:
    if not result or result[-1] < i:
        result.append(i)

    else:
        left, right = 0, len(result)-1

        while left < right:
            mid = (left + right) // 2

            if result[mid] < i:
                left = mid + 1
            else:
                right = mid

        result[right] = i

print(len(result))