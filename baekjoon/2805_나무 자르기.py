N, M = map(int, input().split())
trees = list(map(int, input().split()))

result = 0
left = 0
right = max(trees)

while left <= right:
    mid = (left + right) // 2
    sum = 0

    for tree in trees:
        if tree > mid:
            sum += tree - mid

    if sum >= M:
        left = mid + 1
        result = max(result, mid)
    else:
        right = mid - 1

print(result)